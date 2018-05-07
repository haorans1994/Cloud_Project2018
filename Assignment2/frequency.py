import re
import sys
import nltk
import couchdb
import json
import couchdb.design

dictionary = {} #word freq
stopWords = list(nltk.corpus.stopwords.words('english'))
stopWords.append('TAG')
stopWords.append('URL')
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

while True:
    for tweet in tweetsSearchDB.view('tweets_search/melbourne_tweets'):
        text = tweet.value[0]
        text = re.sub(r'[@][\S]*\s', 'TAG', text)  # replace the @user with tag
        text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)  # replace the web address with url
        text = re.sub(r'#([^\s]+)', r'\1', text)  # remove the '#'
        text = re.sub('_', ' ', text)  # remove the '_'
        text = re.sub(':', ' ', text)  # remove the ':'
        text = re.sub('[\s]+', ' ', text)
        #text = re.sub(r'[^A-Za-z0-9_\s]', '', text)
        fredist = nltk.FreqDist(text.split(' '))
        for localkey in fredist.keys():
            if localkey in stopWords:
                continue
            if localkey in dictionary.keys():
                dictionary[localkey] = dictionary[localkey] + fredist[localkey]
            else:
                dictionary[localkey] = fredist[localkey]
    break

items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
frequency = {}

for item in items:
    frequency['frequency'][item[0]] = item[1]

tweetsFrequencyDB.save(frequency)