import sys
import tweepy
import time
import couchdb
import traceback
import liveSentiment

from tweepy.utils import import_simplejson

AUS_GEO_CODE = [113.03, -39.06, 154.73, -12.28]
USER_NAME = "assignment2"
PASSWORD = "3010"
HOST_NAME = "115.146.86.192"


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


class TwitterGrabe(object):
    def __init__(self):
        info = collect_info()
        self.auth = tweepy.OAuthHandler(info['consumer_key'], info['consumer_secret'])
        self.auth.set_access_token(info["access_token"], info["access_token_secret"])
        self.api = tweepy.API(self.auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def run(self):
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=self.api.auth, listener=myStreamListener)
        loop = True
        """create a loop to continue grab data"""
        while loop:
            loop = False
            """use twitter stream api to get tweets"""
            myStream.filter(locations=AUS_GEO_CODE, async=True)
            print("Asyc task for stream API")


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        """ you can set DB store part here. ot outside"""
        json = import_simplejson()
        str = tweet_analyses(status)
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
        infoDB = client['tweets_api_authorization']
    except couchdb.ResourceNotFound:
        print("Cannot find the database ... Exiting\n")
        sys.exit()
    info = infoDB.get('4132df55d51121c7ffee0723a2002e8b')['info']
    return info

#save tweets from search api
def tweet_save(search):
    for tweet in search:
        json = import_simplejson()
        str = tweet_analyses(tweet)
        tweetsSearchDB.save(json.loads(str))


#simplify the tweet json file
def tweet_analyses(tweet):
    try:
        json = import_simplejson()
        result = {}
        # status info
        result['id_str'] = tweet._json['id_str']
        result['text'] = tweet._json['text']
        result['sentiment'] = liveSentiment.judge_sentiment(tweet._json['text'])
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
