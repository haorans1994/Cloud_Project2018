"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to save the safety rate from each city by using Aurin data
"""
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