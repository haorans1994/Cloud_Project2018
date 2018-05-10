import googlemaps
import couchdb.design
import sys
from tweepy.utils import import_simplejson

USER_NAME = "assignment2"
PASSWORD = "3010"
HOST_NAME = "127.0.0.1"

try:
    tweets_database = couchdb.Server('http://%s:%s@%s:5984' % (USER_NAME, PASSWORD, HOST_NAME))
except couchdb.ServerError:
    print("Cannot find CouchDB Server ... Exiting\n")
    sys.exit()

try:
    tweetsDB = tweets_database['tweets_crawler']
except couchdb.ResourceNotFound:
    print("Cannot find the database ... Exiting\n")
    sys.exit()

try:
    tweetsPostcode = tweets_database['tweets_postcode']
except couchdb.ResourceNotFound:
    print("Cannot find the database ... Exiting\n")
    sys.exit()


# import a suburb name, return its postcode
def getPostCode_suburb(areaName):
    googleMaps = googlemaps.Client(key = 'AIzaSyDkVwBCEmVz7OqmWEIS3vWbvZaquIg3pT8')
    targetLocation = googleMaps.geocode(areaName, region = 'AU')
    # print targetLocation[0]['geometry']['location']
    searchResults = googleMaps.reverse_geocode(targetLocation[0]['geometry']['location'])
    
    for result in searchResults:
        for item in result['address_components']:
            if item['types'] == ['postal_code']:
                return item['long_name']

# print getPostCode_suburb('Parkville')


# import a pair of coordinate, return its postcode
def getPostCode_coord(coordinate):
    googleMaps = googlemaps.Client(key = 'AIzaSyDkVwBCEmVz7OqmWEIS3vWbvZaquIg3pT8')
    searchResults = googleMaps.reverse_geocode(coordinate)
    for result in searchResults:
        for item in result['address_components']:
            if item['types'] == ['postal_code']:
                return item['long_name']

# print getPostCode_coord([-37.788, 144.951])

def convert_postcode():
    for item in tweetsDB.view('tweets_crawler/melbourne_tweets'):
        coordinate = []
        if item.value[2]:
            coordinate = [item.value[2]['coordinates'][1], item.value[2]['coordinates'][0]]
        if item.value[1] == 'neighborhood':
            postcode = getPostCode_suburb(item.key)
            str = {'name':item.key, 'postcode': postcode, 'coordinates': coordinate}
            sava_database(str)
        elif item.value[1] == 'city':
            if item.value[2]:
                postcode = getPostCode_coord(coordinate)
                str = {'name': item.key, 'postcode': postcode, 'coordinates': coordinate}
                sava_database(str)
    print("Finish adding post to all tweets")

def sava_database(str):
    json = import_simplejson()
    result = {}
    result['name'] = str['name']
    result['postcode'] = str['postcode']
    result['coordinates'] = str['coordinates']
    data = json.dumps(result)
    tweetsPostcode.save(json.loads(data))

convert_postcode()