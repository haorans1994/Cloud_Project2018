from LGA import generateLGACode
import getPostCode
import json
import getLgaFromCoordinates

lga_file = open("Aurin/LGA_mel.json").read()
lga_file = json.loads(lga_file)
lgaList = lga_file['features']

def processData():
    info = []
    file = open("tweets/weather.json").read()
    data = json.loads(file)
    tweets = data['rows']
    for tweet in tweets:
        i = i + 1
        postcode = None
        lgaCode = None
        if tweet['value'][2] == "neighborhood":
            postcode = getPostCode.getPostcode(tweet['key'])
            lgaCode = generateLGACode.generateLGA_code(str(postcode))
        elif tweet['value'][2] == 'city':
            if tweet['value'][3]:
                coordinates = [tweet['value'][3]['coordinates'][0], tweet['value'][3]['coordinates'][1]]
                for lga in lgaList:
                    lgaCoordinate = lga['geometry']
                    contains = getLgaFromCoordinates.getLgaCode(coordinates, lgaCoordinate)
                    if contains:
                        lgaCode = lga['properties']['area_code']
                        break
        result = {'text': tweet['value'][0], 'sentiment': tweet['value'][1], 'LgaCode': lgaCode, 'postcode': postcode,
                  'place_name': tweet['key']}
        info.append(result)
    return info


def saveJson(list):
    with open("sentiment/weather_sentiment.json", "w") as jsonFile:
        item = json.dumps(list)
        jsonFile.write(item)

saveJson(processData())