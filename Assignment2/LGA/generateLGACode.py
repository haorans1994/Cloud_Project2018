import json

codeLGA = 'LGA/LGA_code.json'
# put a postcode to judge if it in certain LGA area and then return LGA_code
def generateLGA_code(postcode):
	file = open(codeLGA)
	fileJson = json.load(file)

	for k, v in fileJson.items():
		if postcode in v:
			return k
		else:
			continue

