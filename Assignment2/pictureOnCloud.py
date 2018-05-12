"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to count the high frequency word in the tweets' text from one map view and generate the words picture for visualization
"""
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
import json
import re
import nltk
import couchdb
import sys
from wordcloud import WordCloud, ImageColorGenerator


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
    tweetsFrequencyDB = client['tweets_frequency_words']
except couchdb.ResourceNotFound:
    print("Cannot find the database1 ... Exiting\n")
    sys.exit()

dictionary = {} #word freq
stopWords = list(nltk.corpus.stopwords.words('english'))
file = open("stopwords.txt", 'r')
buffer = file.read()
words = buffer.split('\n')
for word in words:
    if word in stopWords:
        continue
    stopWords.append(word)
file.close()
stopWords.append('AT')
stopWords.append('URL')
image = Image.open(r'/Users/qingqiany/PycharmProjects/cloudass2/pikacho.jpg')
graph = np.array(image)


while True:

    for tweet in tweetsSearchDB.view('tweets_search/sydney_tweets'):
        text = tweet.value[0].lower()
        text = re.sub(r'[@][\S]*\s', ' AT ', text)  # replace the @user with at
        text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', ' URL ', text)  # replace the web address with url
        text = re.sub(r'#([^\s]+)', r'\1', text)  # remove the '#'
        text = re.sub('&amp', ' ', text) # remove the '&amp'
        text = re.sub(r'[\s+\.\!\/_,$%^*(\"\')]+|[:+—()?【】“”！，。？、~@#￥%…&*（）\\’|;-]+',' ',text)
        text = re.sub('[\s]+', ' ', text)

        #text = re.sub(r'[^A-Za-z0-9_\s]', '', text)
        freq = nltk.FreqDist(text.split(' '))
        for localKey in freq.keys():
            if localKey in stopWords:
                continue
            if localKey in dictionary.keys():
                dictionary[localKey] = dictionary[localKey] + freq[localKey]
            else:
                dictionary[localKey] = freq[localKey]

words = sorted(dictionary.items(), key = lambda  x:x[1], reverse = True)
words = words[1:1000]
result = {}
for word in words:
    result[word[0]] = word[1]
wc = WordCloud(background_color='white',max_font_size=50,mask=graph).fit_words(result)

imageColor = ImageColorGenerator(graph)
wc.recolor(color_func=imageColor)
wc.to_file(r"/Users/qingqiany/PycharmProjects/cloudass2/wordcloud1.png")