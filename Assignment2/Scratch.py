import sys
import tweepy
import time
import couchdb
import traceback
from tweepy.utils import import_simplejson

AUS_GEO_CODE = [113.03, -39.06, 154.73, -12.28]
USER_NAME = "database"
PASSWORD = "123456"
HOST_NAME = "127.0.0.1"


try:
    client = couchdb.Server('http://%s:%s@%s:5984' % (USER_NAME, PASSWORD, HOST_NAME))
except couchdb.ServerError:
    print("Cannot find CouchDB Server ... Exiting\n")
    sys.exit()

try:
    tweetsDB = client['tweets']
except couchdb.ResourceNotFound:
    print("Cannot find the database ... Exiting\n")
    sys.exit()

try:
    tweetsSearchDB = client['twitter_search']
except couchdb.ResourceNotFound:
    print("Cannot find the database ... Exiting\n")
    sys.exit()


class TwitterGrabe(object):
    def __init__(self):
        info = collect_info()
        self.auth = tweepy.OAuthHandler(info['consumer_key'], info['consumer_secret'])
        self.auth.set_access_token(info["access_token"], info["access_token_secret"])
        self.api = tweepy.API(self.auth)

    def run(self):
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=self.api.auth, listener=myStreamListener)
        loop = True
        """create a loop to continue grab data"""
        while loop:
            myStream.filter(locations=AUS_GEO_CODE, async=True)
            print("Asyc task for stream API")
            """get data from search api"""
            places = self.api.geo_search(query="AU", granularity="country")
            placeId = places[0].id
            i = 0
            while i < 20:
                search = self.api.search(q="place:%s" % placeId, count=100)
                tweet_save(search)
                i=i+1
            print("search function finish")
            loop = False


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        """ you can set DB store part here. ot outside"""
        json = import_simplejson()
        str = tweet_simplify(status)
        tweetsDB.save(json.loads(str))

    def on_error(self, status):
        """ Handle any error throws from stream API """
        if status == 420:
            self.on_timeout()

    def on_timeout(self):
        """ Handle time out when API reach its limit """

        time.sleep(600)
        return


#get twitter authorization info
def collect_info():
    try:
        infoDB = client['twitter_authorization']
    except couchdb.ResourceNotFound:
        print("Cannot find the database ... Exiting\n")
        sys.exit()
    info = infoDB.get('4132df55d51121c7ffee0723a2002e8b')['info']
    return info

#save tweets from search api
def tweet_save(search):
    for tweet in search:
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