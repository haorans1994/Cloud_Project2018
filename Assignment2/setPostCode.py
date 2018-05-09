from LGA import generateLGACode
import getPostCode
import json
import getLgaFromCoordinates
import csv

lga_file = open("Aurin/LGA_mel.json").read()
lga_file = json.loads(lga_file)
lgaList = lga_file['features']

def processData():
    info = []
    file = open("sydney.json").read()
    data = json.loads(file)
    tweets = data['rows']
    i = 0
    for tweet in tweets:
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

saveCsv(processData())