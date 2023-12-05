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
		list of points from file
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

	distList = [] # list of distances
	for p in points:
		distList.append(metricAlgo(usrpoint, p))
	distList.sort(reverse=True)
	#kNearest = [distList[i] for i in range(KNNparams.get("nofNeighbours"))] # get first K elements from distList

	# TODO choose K nearest out of distances (via voting)

	# TODO return list of indexes in filepoints, list of distances, colour class

	# FIXME temporary:
	return ([14, 3, 67], [14, 3, 67], 229)

# Jeśli byłoby więcej wymiarów (więcej kolumn z liczbami) można for-em zrobić

def eukliDist(usrpoint: tuple, point: tuple):
	# point is also tuble, but ignore it's third value [2]
	return sqrt((point[0] - usrpoint[0])**2 + (point[1] - usrpoint[1])**2)

def cityDist(usrpoint: tuple, point: tuple):
	# point is also tuble, but ignore it's third value [2]
	return __abs(point[0] - usrpoint[0]) + __abs(point[1] - usrpoint[1])

def __abs(v: float):
	if v < 0: return -v
	return v