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
    tweetsSearchDB = client['tweets_search']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()

try:
    tweetsMelbourne = client['tweets_melbourne']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()

lga_file = open("Aurin/LGA_mel.json").read()
lga_file = json.loads(lga_file)
lgaList = lga_file['features']
for tweet in tweetsSearchDB.view('tweets_search/melbourne_tweets'):
    postcode = None
    lgaCode = None
    if tweet.value[2] == "neighborhood":
        postcode = getPostCode.getPostcode(tweet.key)
        lgaCode = generateLGACode.generateLGA_code(str(postcode))
    elif tweet.value[2] == 'city':
        if tweet.value[3]:
            coordinates = [tweet.value[3]['coordinates'][0], tweet.value[3]['coordinates'][1]]
            i = 0
            for lga in lgaList:
                lgaCoordinate = lga['geometry']['coordinates'][0][0]
                contains = getLgaFromCoordinates.getLgaCode(coordinates, lgaCoordinate)
                if contains:
                    lgaCode = lga['properties']['area_code']
                    break
    result = {'text' : tweet.value[0], 'sentiment': tweet.value[1], 'LgaCode': lgaCode, 'postcode': postcode, 'place_name': tweet.key}
    # strs = json.dumps(result)
    # tweetsMelbourne.save(json.loads(strs))
    print(result)