from textblob import TextBlob
import re
import json
import nltk


dictionary = {} #word freq

f = open("tweets_crawler2.json", 'r')
while True:
    line = f.readline()
    if not line:
        break
    if "text\":\"" in line:
        try:
            temp1 = re.findall(r"text\":\"(.*)\"created_at\":\"", line)
            temp2 = re.findall(r"(.*)\",\"created_at\":\"", temp1[0])  # cut the "created_at" part again because it appear twice in line
            tags = re.findall(r'#([^\s]+)', temp2[0])
        except IndexError:
            continue

        for tag in tags:
            if tag in dictionary.keys():
                dictionary[tag] = dictionary[tag] + 1
            else:
                dictionary[tag] = 1

print(sorted(dictionary.items(), key = lambda  x:x[1], reverse = True))

