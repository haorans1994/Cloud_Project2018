import json


# put a postcode to judge if it in certain LGA area and then return LGA_code
def generateLGA_code(codeLGA, postcode):
	file = open(codeLGA, 'rb')
	fileJson = json.load(file)

	for k, v in fileJson.items():
		if postcode in v:
			return k
		else:
			continue

codeLGA = 'LGA_code.json'
print generateLGA_code(codeLGA, '2167')