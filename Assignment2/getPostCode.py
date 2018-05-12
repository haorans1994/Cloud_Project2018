import json
file_path = "postcode/VIC_postcode.json"

post_code_file = open(file_path).read()
post_code_data = json.loads(post_code_file)

def getPostcode(suburb):
    for item in post_code_data:
        suburb = suburb.upper()
        if item['suburb'] == suburb:
            return (item['postcode'])

