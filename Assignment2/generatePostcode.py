import googlemaps


# import a suburb name, return its postcode
def getPostCode_suburb(areaName):
    googleMaps = googlemaps.Client(key='AIzaSyDkVwBCEmVz7OqmWEIS3vWbvZaquIg3pT8')
    targetLocation = googleMaps.geocode(areaName, region='AU')
    # print targetLocation[0]['geometry']['location']
    searchResults = googleMaps.reverse_geocode(targetLocation[0]['geometry']['location'])

    for result in searchResults:
        for item in result['address_components']:
            if item['types'] == ['postal_code']:
                return item['long_name']


# print getPostCode_suburb('Parkville')


# import a pair of coordinate, return its postcode
def getPostCode_coord(coordinate):
    googleMaps = googlemaps.Client(key='AIzaSyDkVwBCEmVz7OqmWEIS3vWbvZaquIg3pT8')
    searchResults = googleMaps.reverse_geocode(coordinate)
    for result in searchResults:
        for item in result['address_components']:
            if item['types'] == ['postal_code']:
                return item['long_name']

                # print getPostCode_coord([-37.788, 144.951])