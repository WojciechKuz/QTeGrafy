from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

from ui_form import metrics, votes
from math import sqrt

metrics = ["euklidesowa", "miejska"]
votes = [u"proste", u"ważone odwrotn. kwadratu odległ."]

# HERE IMPORTANT! obsługuje tylko 2 zmienne liczbowe i zmienną kategorii

# Program zaznacza kliknięty punkt kwadratem, dokonuje klasyfikacji obserwacji
#   odpowiadającej klikniętemu punktowi, oznacza go kolorem odpowiadającym wyznaczonej kategorii, wyróżnia sąsiadów, na podstawie których
#   została dokonana klasyfikacja oraz pokazuje odległości do nich.

# points from file, numb of neighbours (k), kind of metric, kind of voting, user point x, user point y
# KNNparams = (nofNeighbours, metricType, votingSys)
# usrpoint = (x, y)
# RETURNS: tuple of: list of indexes, list of distances (float or str)
def knn(points: list, KNNparams: dict, usrpoint: tuple): #  -> tuple(list(int), list(float | str))
	"""Calculate KNN

	Parameters
	----------
	points: list
		list of points from file, where point is tuple of float, float, int
	KNNparams: tuple(int, str, str)
		should contain: number of neighbours, metric type, voting system
	usrpoint: tuple
		tuple with float x and y describing user point position
	
	Returns
	-------
	tuple(list(int), list(float | str))
		First list in tuple contains indexes of points, that are neighbours.
		Second list contains point's distance to user selected point.
	"""
	# nofNeighbours, metricType, votingSys
	# choose algorithms
	if KNNparams.get("metricType") == metrics[0]:
		metricAlgo = eukliDist
	else:
		metricAlgo = cityDist
	#

	distList = [] # list of tuple(indexes, distances)
	for p in points:
		distList.append((len(distList), metricAlgo(usrpoint, p))) # len = index of new element

	sortDistList = sorted(distList, reverse=True, key=lambda x: x[1]) # sorts by distances

	votableDist = kUniqueArray(sortDistList, KNNparams.get("nofNeighbours"))
	# votableDist - points that took part in voting, there's K unique elements in this list

	# TODO voting. If simpe just use mostPopulatedCategory, else create new array with inverse square dist
	# HMMM... inverse square dist replaces dist entirely before or after kUniqueArray ???
	# WATCH THIS: https://www.youtube.com/watch?v=ypCvdED_DDM

	# TODO return list of indexes in filepoints, list of distances, colour class

	# FIXME temporary:
	return ([14, 3, 67], [14, 3, 67], 229)

# Jeśli byłoby więcej wymiarów (więcej kolumn z liczbami) można for-em zrobić

def kUniqueArray(sortDistL: list, K: int) -> list:
	"""Choose nearest out of sorted distances, there is K unique values."""
	kUniqArr = [] # points that took part in voting, there's K unique elements in it
	uniques = 0
	indx = 0
	while uniques < K:
		if sortDistL[indx] not in kUniqArr:
			uniques += 1
		kUniqArr.append(sortDistL[indx])
		indx += 1
		if indx == len(sortDistL): # in case we reach end of list not finding K unique distances
			break
	return kUniqArr

def mostPopulatedCategory(points: list, negativeOnDuplicate: bool = False) -> int: # if there's duplicate, returned value is negative
	categ = [0,0,0,0,0,0]
	for point in points:
		categ[point[2]] += 1
	return __indexOfMax(categ, negativeOnDuplicate)

def eukliDist(usrpoint: tuple, point: tuple):
	# point is also tuble, but ignore it's third value [2]
	return sqrt((point[0] - usrpoint[0])**2 + (point[1] - usrpoint[1])**2)

def cityDist(usrpoint: tuple, point: tuple):
	# point is also tuble, but ignore it's third value [2]
	return __abs(point[0] - usrpoint[0]) + __abs(point[1] - usrpoint[1])

def __abs(v: float):
	if v < 0: return -v
	return v

def __indexOfMax(ls: list, negOnDup: bool = False): # if there's duplicate, returned value is negative
	maxIndx = 0
	maxVal = ls[0]
	dup = False
	for i in range(1, len(ls)):
		if negOnDup and maxVal == ls[i]:
			maxIndx = i
			dup = True
		if maxVal < ls[i]:
			maxVal = ls[i]
			maxIndx = i
			dup = False
	if dup:
		return -maxIndx
	return maxIndx