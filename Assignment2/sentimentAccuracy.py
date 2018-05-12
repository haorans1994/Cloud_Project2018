"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to calculate sentiment analysis accuracy
"""
import json
import re
from textblob import TextBlob
import os
path = "/Users/qingqiany/Downloads/aclImdb/train/pos"
files = os.listdir(path)
# positive is good, 94%,negative is bad,43%,42%
accuracy = {}
accuracy['pos'] = 0
accuracy['neg'] = 0
accuracy['neu'] = 0
for file in files:
    f = open(path + "/" + file)
    iter_f = iter(f)
    str = ""
    for line in iter_f:
        str = str + line
    #text = re.sub(r'[@][\S]*\s', '', str)
    #correct = TextBlob(text).correct()
    sentiment = TextBlob(str).sentiment
    if sentiment[0] > 0:
        accuracy['pos'] = accuracy['pos'] + 1
    elif sentiment[0] < 0:
        accuracy['neg'] = accuracy['neg'] + 1
    else:
        accuracy['neu'] = accuracy['neu'] + 1
    f.close()
print(accuracy.items())