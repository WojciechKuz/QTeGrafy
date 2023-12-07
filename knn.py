from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

from math import sqrt

metrics = ["euklidesowa", "miejska"]
votes = [u"proste", u"ważone odwrotn. kwadratu odległ."]

KUniqueNeighbourDistances: bool = True

# HERE IMPORTANT! obsługuje tylko 2 zmienne liczbowe i zmienną kategorii

# FIXME k=3 zaznacza 2 zielone, 1 pomarańcz. ale usrpoint jest pomarańczowy!!!

# KNN zaimplementowane według wykładu i wymagań zadania

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
	if KNNparams.get("votingSys") == votes[0]:
		sortAlgo = simple
	else:
		sortAlgo = inverseSquare

	# calculate distances, sort
	distList = [] # list of tuple(indexes, distances)
	for p in points:
		distList.append((len(distList), metricAlgo(usrpoint, p))) # len = index of new element
	sortDistList = sortAlgo(distList)

	votableDist = [] # points that took part in voting, there's K unique elements in this list

	# w prezentacji z wykładu jest:
	# Jeśli kilka obserwacji leży w tej samej odległości od X, co utrudnia wybór
	# najbliższych sąsiadów, to wszystkie one uczestniczą w głosowaniu, nawet
	# jeśli miałoby ich być więcej niż k
	if KUniqueNeighbourDistances:
		votableDist = __kUniqueNearestList(sortDistList, KNNparams.get("nofNeighbours"))
	else:
		votableDist = __kNearestList(sortDistList, KNNparams.get("nofNeighbours"))

	# voting
	category = __mostPopulatedCategory(votableDist, points)

	return (
		votableDist, # indexes and distances
		category
	)

# Jeśli byłoby więcej wymiarów (więcej kolumn z liczbami) można for-em zrobić

def __kNearestList(sortDistL: list, K: int):
	"""simply copies first K elements from list"""
	kpoints = [] # points that took part in voting
	indx = 0
	while indx < K:
		kpoints.append(sortDistL[indx])
		indx += 1
		if indx == len(sortDistL): # in case we reach end of list not finding K distances
			break
	return kpoints

def __kUniqueNearestList(sortDistL: list, K: int) -> list:
	"""Choose nearest out of sorted distances, there is K unique values.
	Parameters
	----------
	sortDistL
		list of tuple(indexes, distances)
	K
		number of neighbours"""
	kUniqArr = [] # points that took part in voting, there's K unique elements in it
	kUniqArrV = [] # value only for comparsions
	uniques = 0
	indx = 0
	while uniques < K:
		if sortDistL[indx][1] not in kUniqArrV: # sortDistL - indx & value, kUniqArrV - only value
			uniques += 1
		kUniqArrV.append(sortDistL[indx][1])
		kUniqArr.append(sortDistL[indx])
		indx += 1
		if indx == len(sortDistL): # in case we reach end of list not finding K unique distances
			break
	return kUniqArr

# OK
def __getCategory(index: int, allpoints: list):
	return allpoints[index][2]

# OK
# points is list of tuples(index: int, distance: float), allpoints list of tuples(float, float, int)
def __mostPopulatedCategory(points: list, allpoints: list, negativeOnDuplicate: bool = False) -> int: # if there's duplicate, returned value is negative
	"""
	Parameters
	----------
	points
		list of tuple(indexes, distances)
	other parameter not described"""
	categ = [0,0,0,0,0,0]
	for point in points:
		categ[__getCategory(point[0], allpoints)] += 1
	return __indexOfMax(categ, negativeOnDuplicate)

# OK
# ls - list of ints
def __indexOfMax(ls: list, negOnDup: bool = False): # simply, finds index of max value
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
	if dup:		# if there's duplicate, returned value is negative
		return -maxIndx
	return maxIndx

# usrpoint, point - list of tuple(indexes, distances)

# OK
def eukliDist(usrpoint: tuple, point: tuple):
	# point is also tuble, but ignore it's third value [2]
	return sqrt((point[0] - usrpoint[0])**2 + (point[1] - usrpoint[1])**2)

# OK
def cityDist(usrpoint: tuple, point: tuple):
	# point is also tuble, but ignore it's third value [2]
	return __abs(point[0] - usrpoint[0]) + __abs(point[1] - usrpoint[1])

# OK
def __abs(v: float) -> float:
	if v < 0: return -v
	return v



# distList - list of tuple(indexes, distances)

def simple(distList: list):
	return sorted(distList, reverse=False, key=lambda x: x[1])

def inverseSquare(distList: list):
	return sorted(__invSquareDistList(distList), reverse=True, key=lambda x: x[1])

# OK
# dist - list of tuple(indexes, distances)
def __invSquareDistList(dist: list) -> list:
	invSq = []
	for d in dist:
		invSq.append((d[0], (1.0/(d[1]**2))))
	return invSq

if __name__ == "__main__":
	print("\nTests:")
	#testMPC = __mostPopulatedCategory([(4, 1.2), (0, 1.3), (3, 1.5)], [(1, 0.3, 4), (0.4, 0.5, 4), (0.7, 0.8,2), (0.4,0.8,2), (0.6, 0.7, 2)])
	# print(testMPC) # MPC sprawne
	#testEUK = eukliDist((2, 3), (6, 6)) # OK
	#print(testEUK) # 5
	#testCITY = cityDist((2, 3), (6, 6)) # OK
	#print(testCITY) # 7
	#print(__abs(-13.5), __abs(63.75))
	ls1: list = [(7, 2.0), (3, 3.0), (12, 2.5)]
	#testINVSQ = __invSquareDistList(ls1)
	#print(testINVSQ)
	testMAX = __indexOfMax([3, 12, 13, 7, 6, 14])
	print(testMAX)
