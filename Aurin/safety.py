import json

def safety(fileName):
	file = open(fileName, 'rb')
	fileJson = json.load(file)['features']
	result = []

	for item in fileJson:
		item = item['properties']
		line = {}
		line['LGA_code'] = item['area_code']
		line['LGA_name'] = item['area_name']
		line['distressDate'] = item['k10_me_2_rate_3_11_7_13']
		result.append(line)
	return result

def outputJson():
	with open('final_distress_perth.json', 'w') as f:
		json.dump(safety(fileName), f)
		print ('completed')


fileName = 'distress_perth.json'
# print safety(fileName)
outputJson()