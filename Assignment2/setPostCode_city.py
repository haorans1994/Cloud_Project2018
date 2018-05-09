from LGA import generateLGACode
import sys
import couchdb.design
import getPostCode
import json
import getLgaFromCoordinates
import csv

AUS_GEO_CODE = [113.03, -39.06, 154.73, -12.28]
USER_NAME = "assignment2"
PASSWORD = "3010"
HOST_NAME = "127.0.0.1"


def connection():
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
    return couchdb_pager(tweetsSearchDB)

def setCode(tweets):
    info = []
    lga_file = open("Aurin/LGA_mel.json").read()
    lga_file = json.loads(lga_file)
    lgaList = lga_file['features']
    for tweet in tweets:
        postcode = None
        lgaCode = None
        if tweet.value[2] == "neighborhood":
            postcode = getPostCode.getPostcode(tweet.key)
            lgaCode = generateLGACode.generateLGA_code(str(postcode))
        elif tweet.value[2] == 'city':
            if tweet.value[3]:
                coordinates = [tweet.value[3]['coordinates'][0], tweet.value[3]['coordinates'][1]]
                for lga in lgaList:
                    lgaCoordinate = lga['geometry']['coordinates'][0][0]
                    contains = getLgaFromCoordinates.getLgaCode(coordinates, lgaCoordinate)
                    if contains:
                        lgaCode = lga['properties']['area_code']
                        break
        result = {'text': tweet.value[0], 'sentiment': tweet.value[1], 'LgaCode': lgaCode, 'postcode': postcode,
                  'place_name': tweet.key}
        info.append(result)
    return info


def saveCsv(list):
    columns = ['text', 'sentiment', 'LgaCode', 'postcode', 'place_name']
    with open("sentiment/melbourne_sentiment.csv", "w") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=columns)
        writer.writeheader()
        for data in list:
            writer.writerow(data)


def couchdb_pager(db, view_name='_design/tweets_search/_view/melbourne_tweets', startkey=None, startkey_docid=None, endkey=None, endkey_docid=None, bulk=5000):
    options = {'limit': bulk + 1}
    if startkey:
        options['startkey'] = startkey
        if startkey_docid:
            options['startkey_docid'] = startkey_docid
    if endkey:
        options['endkey'] = endkey
        if endkey_docid:
            options['endkey_docid'] = endkey_docid
    done = False
    while not done:
        view = db.view(view_name)
        rows = []
        # If we got a short result (< limit + 1), we know we are done.
        if len(view) <= bulk:
            done = True
            rows = view.rows
        else:
            # Otherwise, continue at the new start position.
            rows = view.rows[:-1]
            last = view.rows[-1]
            options['startkey'] = last.key
            options['startkey_docid'] = last.id

        for row in rows:
            yield row


saveCsv(setCode(connection()))