'''format of results is a list with a series of dictionary, with attributes: 'postcode', 'distress_rate', 'distress_count'.'''

import googlemaps
import json

def resolveJson(fileName):
    resultList = []
    file = open(fileName, 'rb')
    fileJson = json.load(file)['features']

    for item in fileJson:
        item = item['properties']
        line = {}
        line['postcode'] = getPostCode(item['area_name'])
        line['areaName'] = item['area_name']
        line['distress_rate'] = item['k10_me_2_rate_3_11_7_13']
        line['distress_count'] = item['k10_me_1_no_3_11_7_13']
        line['totoal_population'] = item['k10_me_1_no_3_11_7_13']/(item['k10_me_2_rate_3_11_7_13']/100)
        resultList.append(line)
    return resultList


def getPostCode(areaName):
    googleMaps = googlemaps.Client(key = 'AIzaSyDkVwBCEmVz7OqmWEIS3vWbvZaquIg3pT8')
    targetLocation = googleMaps.geocode(areaName, region = 'AU')
    searchResults = googleMaps.reverse_geocode(targetLocation[0]['geometry']['location'])

    for result in searchResults:
        for item in result['address_components']:
            if item['types'] == ['postal_code']:
                return item['long_name']

def outputJson():
	with open('aurin_psycho_output.json', 'w') as f:
		json.dump(resolveJson(fileName), f)
		print 'completed'

fileName = '../Psychological_Distress/json/data4978361955240034894.json'
# resolveJson(fileName)
outputJson()




