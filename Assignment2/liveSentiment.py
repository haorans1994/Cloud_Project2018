import json
import re
from textblob import TextBlob
import emoji

def judge_sentiment(text):
        text1 = text.lower()  # to lower case
        text1 = emoji.demojize(text1)  #convert emoji to word
        text1 = re.sub(r'[@][\S]*\s', 'TAG', text1)  # replace the @user with tag
        text1 = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text1)  # replace the web address with url
        text1 = re.sub(r'#([^\s]+)', r'\1', text1)  # remove the '#'
        text1 = re.sub('_', ' ', text1)  # remove the '_'
        text1 = re.sub(':', ' ', text1)  # remove the ':'
        text1 = re.sub('[\s]+', ' ', text1)  # remove the duplicate space
        correct = TextBlob(text1) # correct the text spell error
        sentiment = correct.sentiment
        if sentiment[0] < 0:
                tag = 'negative'
        elif sentiment[0] > 0:
                tag = 'positive'
        else:
                tag = 'neutral'
        return tag
# tag = judge_sentiment("When you’re low on policies- try to scare everyone - Matthew Guy is a one trick pony https://t.co/5lMAhZlut")
# print(tag)