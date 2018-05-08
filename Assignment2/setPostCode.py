import generatePostcode
from LGA import generateLGACode
import sys
import couchdb.design


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

for tweet in tweetsSearchDB.view('_all_docs', include_docs=True).rows:
    postcode = None
    lgaCode = None
    item = tweetsSearchDB.get(tweet['id'])
    if item['place']:
        if item['place']['place_type'] == "neighborhood":
            postcode = generatePostcode.getPostCode_suburb(item['place']['name'])
            lgaCode = generateLGACode.generateLGA_code(postcode)
            print(item['place']['name'], postcode, lgaCode)
        elif item['place']['place_type'] == "city":
            if item['coordinates']:
                coordinates = [item['coordinates']['coordinates'][1], item['coordinates']['coordinates'][0]]
                postcode = generatePostcode.getPostCode_coord(coordinates)
                lgaCode = generateLGACode.generateLGA_code(postcode)
                print(item['place']['name'], postcode, lgaCode)

    item['postcode'] = postcode
    item['lagcode'] = lgaCode
    tweetsSearchDB.save(item)

