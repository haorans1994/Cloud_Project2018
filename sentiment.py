import json
import re
from textblob import TextBlob
import emoji

sentimentResult = {}
f = open("tweets_crawler2.json", 'r')
while True:
    line = f.readline()
    if not line:
        break
    if "text\":\"" in line:
        line1 = line.split("text\":\"")[1:] #get the string after text tag
        line2 = "".join(line1)  # list to string
        line3 = line2[:-3]  # cut the useless items
        line4 = emoji.demojize(line3)
        text = line4.lower()                                           #to lower case
        text = re.sub(r'[@][\S]*\s', 'TAG', text)                      #replace the @user with tag
        text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))','URL',text) #replace the web address with url
        text = re.sub(r'#([^\s]+)', r'\1', text)                       #remove the '#'
        text = re.sub('_', ' ', text)                                  #remove the '_'
        text = re.sub(':', ' ', text)                                  #remove the ':'
        text = re.sub('[\s]+', ' ', text)                              #remove the duplicate space
        correct = TextBlob(text).correct()                             #correct the text spell error
        sentiment = correct.sentiment
        if sentiment[0] < 0:
                tag = 'negative'
        elif sentiment[0] > 0:
                tag = 'positive'
        else:
                tag = 'neutral'
        sentimentResult[line3] = tag

f.close()