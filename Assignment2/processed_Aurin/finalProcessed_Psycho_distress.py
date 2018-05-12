# Return a dictionary with format: {'postcode': (rate, count, population)}

import googlemaps
import json

def mergeSameCode(fileName):
	resultList = {}
	file = open(fileName, 'rb')
	fileJson = json.load(file)

	for item in fileJson:
		resultList.setdefault(item['postcode'], (0.0, 0.0, 0.0))
		mergedCount = resultList[item['postcode']][1] + item['distress_count']
		mergedPopulation = resultList[item['postcode']][2] + item['totoal_population']
		if mergedPopulation == 0.0:
			continue
		mergedRate = (mergedCount/mergedPopulation) * 100
		resultList[item['postcode']] = (mergedRate, mergedCount, mergedPopulation)
	return resultList

def outputFinalDistress():
	with open ('aurin_psycho_final_output.json', 'w') as f :
		json.dump(mergeSameCode(fileName), f)
		print 'completed'




fileName = 'aurin_psycho_output.json'
outputFinalDistress()
