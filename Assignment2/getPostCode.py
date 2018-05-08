import json
file_path = "au_postcodes.json"

post_code_file = open("au_postcodes.json").read()
post_code_data = json.loads(post_code_file)

def getPostcode(suburb):
    for item in post_code_data:
        suburb = suburb.upper()
        if item['suburb'] == suburb:
            return (item['postcode'])


getPostcode("Docklands")