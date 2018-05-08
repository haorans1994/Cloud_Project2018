from LGA import generateLGACode
import sys
import couchdb.design
import getPostCode
import json
import getLgaFromCoordinates


AUS_GEO_CODE = [113.03, -39.06, 154.73, -12.28]
USER_NAME = "assignment2"
PASSWORD = "3010"
HOST_NAME = "127.0.0.1"

try:
    client = couchdb.Server('http://%s:%s@%s:5984' % (USER_NAME, PASSWORD, HOST_NAME))
except couchdb.ServerError:
    print("Cannot find CouchDB Server ... Exiting\n")
    sys.exit()

try:
    tweetsSearchDB = client['tweets_crawler']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()


# for tweet in tweetsSearchDB.view('tweets_search/melbourne_tweets'):
#     if tweet.value[2] == "neighborhood":
#         postcode = generatePostcode.getPostCode_suburb(tweet.key)
#         lgaCode = generateLGACode.generateLGA_code(postcode)
#         print(tweet.key, postcode, lgaCode)
#     elif tweet.value[2] == "city":
#         if tweet.value[3]:
#             coordinates = [tweet.value[3]['coordinates'][1], tweet.value[3]['coordinates'][0]]
#             postcode = generatePostcode.getPostCode_coord(coordinates)
#             lgaCode = generateLGACode.generateLGA_code(postcode)
#             print(tweet.key, postcode, lgaCode)
lga_file = open("LGAcode.json").read()
lga_file = json.loads(lga_file)
lgaList = lga_file['features']

for tweet in tweetsSearchDB.view('_all_docs', include_docs=True).rows:
    postcode = None
    lgaCode = None
    item = tweet.doc
    if 'place' in item:
        place = item['place']
        if 'place_type' in place:
            if place['place_type'] == "neighborhood":
                postcode = getPostCode.getPostcode(place['name'])
                lgaCode = generateLGACode.generateLGA_code(str(postcode))
                print(place['name'], postcode, lgaCode)
            # elif place['place_type'] == "city":
            #     if item['coordinates']:
            #         coordinates = [item['coordinates']['coordinates'][0], item['coordinates']['coordinates'][1]]
            #         for lga in lgaList:
            #             lgaCoordinate = lga['geometry']['coordinates'][0][0]
            #             contains = getLgaFromCoordinates.getLgaCode(coordinates, lgaCoordinate)
            #             if contains:
            #                 lgaCode = lga['properties']['area_code']
            #                 break
            #         print(place['name'], postcode, lgaCode)


    # item['postcode'] = postcode
    # item['lgacode'] = lgaCode
    # tweetsSearchDB.save(item)
#
# for lga in lgaList:
#     #lgaCode = getLgaFromCoordinates.getLgaCode(coordinates, lga[0][0][0])
#     print(lga[0][0][0])
# print("finish!!!")
