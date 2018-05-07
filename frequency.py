from textblob import TextBlob
import re
import json
import nltk


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

f = open("tweets_crawler2.json", 'r')
while True:
    line = f.readline()
    if not line:
        break
    if "text\":\"" in line:

        try:
            temp1 = re.findall(r"text\":\"(.*)\"created_at\":\"", line)
            temp2 = re.findall(r"(.*)\",\"created_at\":\"", temp1[0])  # cut the "created_at" part again because it appear twice in line
            # temp3 = emoji.demojize(temp2[0])
            text = temp2[0].lower()  # to lower case
        except IndexError:
            continue

        text = re.sub(r'[@][\S]*\s', ' AT ', text)  # replace the @user with at
        text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', ' URL ', text)  # replace the web address with url
        text = re.sub(r'#([^\s]+)', r'\1', text)  # remove the '#'
        text = re.sub('&amp', ' ', text)  # remove the '&amp'
        text = re.sub(r'[\s+\.\!\/_,$%^*(\"\')]+|[:+—()?【】“”！，。？、~@#￥%…&*（）\\’|;-]+', ' ', text)
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

print(sorted(dictionary.items(), key = lambda  x:x[1], reverse = True))

