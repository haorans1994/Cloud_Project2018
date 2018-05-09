from LGA import generateLGACode
import getPostCode
import json
import getLgaFromCoordinates
import csv
import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

lga_file = open("Aurin/LGA_mel.json").read()
lga_file = json.loads(lga_file)
lgaList = lga_file['features']


def processData():
    info = []
    file = open("sydney.json").read()
    data = json.loads(file)
    tweets = data['rows']
    whole_lines = len(tweets)
    start_line = int(whole_lines/comm_size) * comm_rank
    if comm_rank == comm_size - 1:end_line = whole_lines
    else:end_line = int(whole_lines/comm_size) * (comm_rank+1)


    i = 0
    for j in range(start_line,end_line):
        tweet = tweets[j]
        i = i + 1
        print(i)
        postcode = None
        lgaCode = None
        if tweet['value'][2] == "neighborhood":
            postcode = getPostCode.getPostcode(tweet['key'])
            lgaCode = generateLGACode.generateLGA_code(str(postcode))
        elif tweet['value'][2] == 'city':
            if tweet['value'][3]:
                coordinates = [tweet['value'][3]['coordinates'][0], tweet['value'][3]['coordinates'][1]]
                for lga in lgaList:
                    lgaCoordinate = lga['geometry']['coordinates'][0][0]
                    contains = getLgaFromCoordinates.getLgaCode(coordinates, lgaCoordinate)
                    if contains:
                        lgaCode = lga['properties']['area_code']
                        break
        result = {'text': tweet['value'][0], 'sentiment': tweet['value'][1], 'LgaCode': lgaCode, 'postcode': postcode,
                  'place_name': tweet['key']}
        info.append(result)
    return info


def saveCsv(list):
    columns = ['text', 'sentiment', 'LgaCode', 'postcode', 'place_name']
    with open("sentiment/sydney_sentiment.csv", "w") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=columns)
        writer.writeheader()
        for data in list:
            writer.writerow(data)

result = processData()
combine_result = comm.gather(result,root = 0)
if comm_rank == 0:
    saveCsv(combine_result)


