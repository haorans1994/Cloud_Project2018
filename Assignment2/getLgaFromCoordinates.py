from shapely.geometry import MultiPoint
from shapely.geometry import Point
# coords is a list of (x, y) tuples
def turnTuple(list):
	resultList = []
	for eachItem in list:
		resultList.append(tuple(eachItem))
	return resultList

# print coords
#point = Point(151.1213, -33.895566)

def getLgaCode(coordinates, list):
    point = Point(coordinates[0], coordinates[1])
    coords = turnTuple(list)
    poly = MultiPoint(coords).convex_hull
    return poly.contains(point)
