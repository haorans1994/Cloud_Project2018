import sys
import tweepy
import couchdb
import traceback
from tweepy.utils import import_simplejson

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
    tweetsMaxId = client['tweets_id']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()


class TwitterGrabe(object):
    def __init__(self):
        info = collect_info()
        self.auth = tweepy.OAuthHandler(info['consumer_key'], info['consumer_secret'])
        self.auth.set_access_token(info["access_token"], info["access_token_secret"])
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def run(self):
        places = self.api.geo_search(query="AU", granularity="country")
        placeId = places[0].id
        doc = tweetsMaxId.get('6914db08a8487393f194483dfed76a34')
        maxId = doc["max_id"]
        print("Begin to get tweets")
        while True:
            """get data from search api"""
            if maxId == 0:
                search = self.api.search(q="place:%s" % placeId, count=100)
            else:
                search = self.api.search(q="place:%s" % placeId, count=100, max_id=maxId, until="2018-04-23")
            maxId = tweet_find_min_id(search)
            tweet_save(search)
            doc["max_id"] = maxId
            tweetsMaxId.save(doc)
        print("search function finish")

def tweet_find_min_id(search):
    minId = 0
    i = 0
    for tweet in search:
        if i == 0:
            minId = tweet._json['id']
        if tweet._json['id'] < minId:
            minId = tweet._json['id']
        i = i + 1
    return minId

#get twitter authorization info
def collect_info():
    try:
        infoDB = client['twitter_api_authorization']
    except couchdb.ResourceNotFound:
        print("Cannot find the database2 ... Exiting\n")
        sys.exit()
    info = infoDB.get('4132df55d51121c7ffee0723a2002e8b')['info']
    return info


#save tweets from search api
def tweet_save(current):
    for tweet in current:
        json = import_simplejson()
        str = tweet_simplify(tweet)
        tweetsSearchDB.save(json.loads(str))


#simplify the tweet json file
def tweet_simplify(tweet):
    try:
        json = import_simplejson()
        result = {}
        # status info
        result['text'] = tweet._json['text']
        result['id_str'] = tweet._json['id_str']
        result['created_at'] = tweet._json['created_at']
        result['source'] = tweet._json['source']
        result['in_reply_to_status_id_str'] = tweet._json['in_reply_to_status_id_str']
        result['in_reply_to_user_id_str'] = tweet._json['in_reply_to_user_id_str']
        result['in_reply_to_screen_name'] = tweet._json['in_reply_to_screen_name']
        result['coordinates'] = tweet._json['coordinates']
        result['place'] = tweet._json['place']
        # user info
        result['user'] = tweet._json['user']
        str = json.dumps(result)
        return str
    except:
        traceback.print_exc()


x = TwitterGrabe()
x.run()
