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

try:
    tweetsSearchDB = tweets_database['tweets_search']
except couchdb.ResourceNotFound:
    print("Cannot find the database ... Exiting\n")
    sys.exit()


class MyMapView(object):

    def create_view(self):
        sydney_tweets = "function(doc) {var location = doc.place.full_name.split(','); if(doc.place.place_type == 'neighborhood' && location[1] == ' Sydney') {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}if(doc.place.place_type == 'city' && location[0] == 'Sydney' && doc.coordinates) {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}}"
        sydney_view = couchdb.design.ViewDefinition('tweets_search', 'sydney_tweets', sydney_tweets)
        sydney_view.sync(tweetsSearchDB)

        melbourne_tweets = "function(doc) {var location = doc.place.full_name.split(','); if(doc.place.place_type == 'neighborhood' && location[1] == ' Melbourne') {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}if(doc.place.place_type == 'city' && location[0] == 'Melbourne' && doc.coordinates) {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}}"
        melbourne_view = couchdb.design.ViewDefinition('tweets_search', 'melbourne_tweets', melbourne_tweets)
        melbourne_view.sync(tweetsSearchDB)

        canberra_tweets = "function(doc) {var location = doc.place.full_name.split(','); if(doc.place.place_type == 'neighborhood' && location[1] == ' Canberra') {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}if(doc.place.place_type == 'city' && location[0] == 'Canberra' && doc.coordinates) {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}}"
        canberra_view = couchdb.design.ViewDefinition('tweets_search', 'canberra_tweets', canberra_tweets)
        canberra_view.sync(tweetsSearchDB)

        perth_tweets = "function(doc) {var location = doc.place.full_name.split(','); if(doc.place.place_type == 'neighborhood' && location[1] == ' Perth') {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}if(doc.place.place_type == 'city' && location[0] == 'Perth' && doc.coordinates) {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}}"
        perth_view = couchdb.design.ViewDefinition('tweets_search', 'perth_tweets', perth_tweets)
        perth_view.sync(tweetsSearchDB)

        map_tweets = "function(doc) {var location = doc.place.full_name.split(','); if(doc.place.place_type == 'neighborhood' && location[1] == ' Canberra') {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}if(doc.place.place_type == 'city' && location[0] == 'Canberra' && doc.coordinates) {emit(doc.place.name, [doc.text, doc.place.place_type, doc.coordinates]);}}"
        map_reduce = "function (keys, valuse, rereduce) { var total={}; var text=values[0]; for (i in text) { if (total[text[i]] == undefined) { total[text[i]] =1; } else { total[text[i]]++; }} return total;}"
        map_view = couchdb.design.ViewDefinition('tweets_search', 'map_tweets', map_tweets, map_reduce)
        map_view.sync(tweetsSearchDB)

    def run(self):
        print("Create map view indexes!")
        self.create_view()

x = MyMapView()
x.run()
