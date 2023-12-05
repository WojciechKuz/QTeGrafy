from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

from ui_form import metrics, votes

# points from file, numb of neighbours (k), kind of metric, kind of voting, user point x, user point y
# KNNparams = (nofNeighbours, metricType, votingSys)
# usrpoint = (x, y)
# RETURNS: tuple of: list of indexes, list of distances (float or str)
def knn(points: list, KNNparams: tuple, usrpoint: tuple): #  -> tuple(list(int), list(float | str))
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
	nofNeighbours = KNNparams[0]
	metricType = KNNparams[1]
	votingSys = KNNparams[2]
	# TODO calculate KNN stuff

	# TODO return list of indexes in filepoints and list of distances

	# FIXME temporary:
	return ([14, 3, 67], [14, 3, 67])