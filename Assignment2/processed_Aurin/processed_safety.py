# Return json file like
# {
  #   "postcode": "3047",
  #   "areaName": "Hume (C) - Broadmeadows",
  #   "safeRate": 88.5
  # }, but has duplication

import googlemaps
import re
import sys
import json

def resolveJson(fileName):
    resultList = []
    file = open(fileName, 'rb')
    fileJson = json.load(file)['features']

    for item in fileJson:
        item = item['properties']
        line = {}
        try:
            line['postcode'] = getPostCode(item['sla_name06'])
            line['areaName'] = item['sla_name06']
            line['safeRate'] = item['estimate']
        except:
            line['postcode'] = '000000'
            line['safeRate'] = item['estimate']
            line['areaName'] = item['sla_name06']
        # print line
        resultList.append(line)
        # print resultList
    return resultList


def getPostCode(areaName):
    formattedName = formatAddress(areaName)
    googleMaps = googlemaps.Client(key = 'AIzaSyDkVwBCEmVz7OqmWEIS3vWbvZaquIg3pT8')
    targetLocation = googleMaps.geocode(formattedName, region = 'AU')
    # print targetLocation
    searchResults = googleMaps.reverse_geocode(targetLocation[0]['geometry']['location'])

    for result in searchResults:
        for item in result['address_components']:
            if item['types'] == ['postal_code']:
                return item['long_name']


def formatAddress(address):
    regular = re.compile(r'\(.*?\)')
    formattedName = regular.sub('', address)
    return formattedName

def outputJson():
    with open('safety_night_output.json', 'w') as f:
        json.dump(resolveJson(fileName), f)
        print 'completed'


fileName = '../Safety_night/json/data7811744708748125153.json'
# resolveJson(fileName)
outputJson()


