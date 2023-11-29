
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.backends.backend_qtagg import FigureCanvas # ???
import numpy as np

colours = {
	0: "blue",
	1: "cyan",
	2: "green",
	3: "orange",
	4: "red",
	5: "magenta"
}

class GraphManager:
	ax: Axes
	def __init__(self, figcanv: FigureCanvas):
		fig: Figure = figcanv.figure
		self.ax = fig.subplots()

		# TODO create graphs using ax.plot()
		pass

	__points: list
	usrpoint: list # as x, y, colour. -1 = colour not found yet
	def loadPoints(self, points):
		self.__points = points

	def displayPoints(self):
		xaxle = []
		yaxle = []
		pointcool = []
		for x in self.__points: # points is list of lists(float, float, int) so x is list(float, float, int) 
			xaxle.append(x[0])
			yaxle.append(x[1])
			pointcool.append(colours.get(x[2], "grey")) # in case, grey colour marks errors
		self.ax.scatter(np.array(xaxle), np.array(yaxle), c=pointcool)
		pass

	def displayUsrPoint(self):
		pass

	# TODO mark points under passed indexes from filepoints as neighbours with black border
	def paintBorders(self, pointIndexes: list):
		pass

	# TODO mark points under passed indexes from filepoints as neighbours with black border and show distance to usrpoint
	# pass list of lists with: indexes to points that should have border, distance to usrpoint
	def paintBordersWithDistance(self, pointIndexes: list):
		pass

	# TODO remove border from points
	def removePointBorder(self):
		pass