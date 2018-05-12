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
        temp1 = re.findall(r"text\":\"(.*)\"created_at\":\"",line)
        temp2 = re.findall(r"(.*)\",\"created_at\":\"",temp1[0])       #cut the "created_at" part again because it appear twice in line
        temp3 = emoji.demojize(temp2[0])
        text = temp3.lower()                                           #to lower case
        text = re.sub(r'[@][\S]*\s1', 'TAG', text)                      #replace the @user with tag
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
        sentimentResult[temp2[0]] = tag

f.close()