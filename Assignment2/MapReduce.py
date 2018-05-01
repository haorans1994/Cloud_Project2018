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
        sydney_tweets = "function (doc) { var location = doc.place.full_name.split(','); if(location[0].includes('Sydney') || location[1].includes('Sydney')){ emit(doc.place.name, [doc.text, doc.coordinates, doc.place.place_type])}}"
        sydney_view = couchdb.design.ViewDefinition('tweets_crawler', 'sydney_tweets', sydney_tweets)
        sydney_view.sync(tweetsDB)

        melbourne_tweets = "function (doc) {var location = doc.place.full_name.split(','); if(location[0] == 'Melbourne' || location[1] == ' Melbourne'){ emit(doc.place.name, [doc.text, doc.coordinates, doc.place.place_type])}}"
        melbourne_view = couchdb.design.ViewDefinition('tweets_crawler', 'melbourne_tweets', melbourne_tweets)
        melbourne_view.sync(tweetsDB)

        canberra_tweets = "function (doc) {var location = doc.place.full_name.split(',');if(location[0] == 'Canberra' || location[1] == ' Canberra'){ emit(doc.place.name, [doc.text, doc.coordinates, doc.place.place_type])}}"
        canberra_view = couchdb.design.ViewDefinition('tweets_crawler', 'canberra_tweets', canberra_tweets)
        canberra_view.sync(tweetsDB)

        perth_tweets = "function (doc) {var location = doc.place.full_name.split(',');if(location[0] == 'Perth' || location[1] == ' Perth'){emit(doc.place.name, [doc.text, doc.coordinates, doc.place.place_type])}}"
        perth_view = couchdb.design.ViewDefinition('tweets_crawler', 'perth_tweets', perth_tweets)
        perth_view.sync(tweetsDB)
        
        map_tweets = "function (doc) {var location = doc.place.full_name.split(',');if(location[0] == 'Perth' || location[1] == 'Perth'){emit(doc.place.name, [doc.text, doc.coordinates, doc.place.place_type])}}"
        map_reduce = "function (keys, valuse, rereduce) { var total={}; var text=values[0]; for (i in text) { if (total[text[i]] == undefined) { total[text[i]] =1; } else { total[text[i]]++; }} return total;}"
        map_view = couchdb.design.ViewDefinition('tweets_crawler', 'map_tweets', map_tweets, map_reduce)
        map_view.sync(tweetsDB)

    def run(self):
        print("Create map view indexes!")
        self.create_view()


x = MyMapView()
x.run()
