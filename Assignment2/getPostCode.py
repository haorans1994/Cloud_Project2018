"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to calculate tweets' the postcode by their suburb name
"""
import json
file_path = "postcode/VIC_postcode.json"

post_code_file = open(file_path).read()
post_code_data = json.loads(post_code_file)

def getPostcode(suburb):
    for item in post_code_data:
        suburb = suburb.upper()
        if item['suburb'] == suburb:
            return (item['postcode'])

