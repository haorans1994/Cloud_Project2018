import re
import json
import couchdb
import sys

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
    tweetsDB = client['tweets_crawler']
except couchdb.ResourceNotFound:
    print("Cannot find the database ... Exiting\n")
    sys.exit()

try:
    tweetsSearchDB = client['tweets_search']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()

try:
    tweetsFrequencyDB = client['tweets_frequency']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()


dictionary = {} #tag freq

while True:
    for tweet in tweetsSearchDB.view('tweets_search/sydney_tweets'):
        text = tweet.value[0].lower()
        tags = re.findall(r'#([^\s]+)', text)
        for tag in tags:
            if tag in dictionary.keys():
                dictionary[tag] = dictionary[tag] + 1
            else:
                dictionary[tag] = 1
    break

tags = (sorted(dictionary.items(), key = lambda  x:x[1], reverse = True))
tags = tags[0:99]

frequency = {}

for item in tags:
    frequency[item[0]] = item[1]

words = {"place": "Sydney", "freq": frequency}
str = json.dumps(words)
tweetsFrequencyDB.save(json.loads(str))

