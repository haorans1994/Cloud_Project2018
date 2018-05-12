# Return a dictionary with format {'postcode' : (safeRate, mergedCount, mergedTotal)}
# "3922": [99.4, 99.4, 1],
import json
import googlemaps

def mergeSameCode(fileName):
	resultList = {}
	file = open(fileName, 'rb')
	fileJson = json.load(file)

	for item in fileJson:
		resultList.setdefault(item['postcode'], (0.0, 0.0,0))
		mergedCount = resultList[item['postcode']][1] + item['safeRate']
		mergedTotal = resultList[item['postcode']][2] + 1
		safeRate = mergedCount / mergedTotal

		resultList[item['postcode']] = (safeRate, mergedCount, mergedTotal)
	# print resultList
	return resultList

def outputFinalSafty():
	with open ('final_safetyNight_output.json', 'w') as f:
		json.dump(mergeSameCode(fileName), f)
		print 'completed'






fileName = 'safety_night_output.json'
# mergeSameCode(fileName)
outputFinalSafty()