"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to allocate distress rate, safety rate and sitting rate to each LGA with its sentiment statistic data
"""
import json
import os


path=os.path.abspath('..')


def processData():

    lgacodes = {}
    data = open("melbourne_sentiment.json").read()
    tweets = json.loads(data)

    distress = {}
    distress_data = open(path + "/Aurin/final_distress_mel.json").read()
    distress_list = json.loads(distress_data)
    for item in distress_list:
        lgacode = item['LGA_code']
        if lgacode not in distress:
            distress[str(lgacode)] = [item['LGA_name'], item['distressDate']]

    day_safe = {}
    day_safe_data = open(path + "Aurin/final_safety_day.json").read()
    day_safe_list = json.loads(day_safe_data)
    for item in day_safe_list:
        lgacode = item['LGA_code']
        if lgacode not in distress:
            day_safe[str(lgacode)] = item["safety_day"]

    night_safe = {}
    night_safe_data = open(path + "Aurin/final_safety_night.json").read()
    night_safe_list = json.loads(night_safe_data)
    for item in night_safe_list:
        lgacode = item['LGA_code']
        if lgacode not in distress:
            night_safe[str(lgacode)] = item["safety_day"]

    sitting = {}
    sitting_data = open(path + "Aurin/final_sitting.json").read()
    sitting_list = json.loads(sitting_data)
    for item in sitting_list:
        lgacode = item['LGA_code']
        if lgacode not in distress:
            sitting[str(lgacode)] = item["safety_day"]

    for tweet in tweets:
        lgacode = str(tweet['LgaCode'])
        area_name = ""
        distress_rate = 0
        safety_night = 0
        safety_day = 0
        sitting_time = 0
        if lgacode is not '':
            if lgacode != "None":
                area_name = distress[lgacode][0]
                distress_rate = distress[lgacode][1]
                if lgacode in night_safe.keys():
                    safety_night = night_safe[lgacode]
                    safety_day = day_safe[lgacode]
                if lgacode in sitting.keys():
                    sitting_time = sitting[lgacode]
        if lgacode not in lgacodes:
            lgacodes[lgacode] = [0, 0, 0, area_name, distress_rate, safety_day, safety_night, sitting_time]




    for tweet in tweets:
        code = str(tweet['LgaCode'])
        sentiment = tweet['sentiment']

        if sentiment == 'positive':
            lgacodes[code][0] = lgacodes[code][0] + 1
        elif sentiment == 'negative':
            lgacodes[code][1] = lgacodes[code][1] + 1
        elif sentiment == 'neutral':
            lgacodes[code][2] = lgacodes[code][2] + 1

    for area in lgacodes:
        positive_rate = lgacodes[area][0] / (lgacodes[area][0] + lgacodes[area][1] + lgacodes[area][2])
        lgacodes[area].append(round(positive_rate, 2))

    for area in lgacodes:
        total_tweets = lgacodes[area][0] + lgacodes[area][1] + lgacodes[area][2]
        lgacodes[area].append(total_tweets)

    data = json.dumps(lgacodes)
    with open('melbourne_total.json', 'w') as outfile:
        outfile.write(data)




processData()

