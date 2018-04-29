import couchdb
import couchdb.design
import sys

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


class MyMapView(object):

    def create_view(self):
        sydney_tweets = """
                        function (doc) {
                            var location = doc.place.full_name.split(",");
                            if(location[0] == "Sydney" || location[1] == "Sydney"){
                                emit(doc.place.name, [doc.text, doc.place.bounding_box])
                            }
                        }
                        """
        sydney_view = couchdb.design.ViewDefinition('tweets', 'sydney_tweets', sydney_tweets)
        sydney_view.sync(tweetsDB)

        melbourne_tweets = """
                        function (doc) {
                            var location = doc.place.full_name.split(",");
                            if(location[0] == "Melbourne" || location[1] == "Melbourne"){
                                emit(doc.place.name, [doc.text, doc.place.bounding_box])
                            }
                        }
                        """
        melbourne_view = couchdb.design.ViewDefinition('tweets', 'melbourne_tweets', melbourne_tweets)
        melbourne_view.sync(tweetsDB)

        canberra_tweets = """
                            function (doc) {
                                var location = doc.place.full_name.split(",");
                                if(location[0] == "Canberra" || location[1] == "Canberra"){
                                    emit(doc.place.name, [doc.text, doc.place.bounding_box])
                                }
                            }
                            """
        canberra_view = couchdb.design.ViewDefinition('tweets', 'canberra_tweets', canberra_tweets)
        canberra_view.sync(tweetsDB)

        perth_tweets = """
                        function (doc) {
                            var location = doc.place.full_name.split(",");
                            if(location[0] == "Perth" || location[1] == "Perth){
                                emit(doc.place.name, [doc.text, doc.place.bounding_box])
                            }
                        }
                        """
        perth_view = couchdb.design.ViewDefinition('tweets', 'perth_tweets', perth_tweets)
        perth_view.sync(tweetsDB)

    def run(self):
        print("Create map view indexes!")
        self.create_view()


x = MyMapView()
x.run()
