import tweepy
import authortize_issue
import time

AUS_GEO_CODE = [113.03, -39.06, 154.73, -12.28]


class TwitterGrabe(object):
    def __init__(self):
        info = authortize_issue.Get_atuhorize_information()
        self.auth = tweepy.OAuthHandler(info['consumer_key'], info['consumer_secret'])
        self.auth.set_access_token(info["access_token"], info["access_token_secret"])
        self.api = tweepy.API(self.auth)

    def run(self):
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=self.api.auth, listener=myStreamListener)
        loop = True
        """create a loop to continue grab data"""
        while loop:
            myStream.filter(locations=AUS_GEO_CODE)
            loop = False





class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        """ you can set DB store part here. ot outside"""
        print(status)

    def on_error(self, status):
        """ Handle any error throws from stream API """
        if status == 420:
            self.on_timeout()

    def on_timeout(self):
        """ Handle time out when API reach its limit """

        time.sleep(600)
        return


x = TwitterGrabe()
x.run()