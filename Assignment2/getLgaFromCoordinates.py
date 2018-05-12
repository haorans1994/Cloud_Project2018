"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to calculate tweets' the LGA code by their coordinates
"""
from shapely.geometry import shape
from shapely.geometry import Point
# coords is a list of (x, y) tuples
def turnTuple(list):
	resultList = []
	for eachItem in list:
		resultList.append(tuple(eachItem))
	return resultList

# print coords
#point = Point(151.1213, -33.895566)

def getLgaCode(coordinates, geometry):
    point = Point(coordinates[0], coordinates[1])
    poly = shape(geometry).convex_hull
    return poly.contains(point)
