
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.backends.backend_qtagg import FigureCanvas # ???
import numpy as np


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
		for x in self.__points:
			xaxle.append(self.__points[x][0])
			yaxle.append(self.__points[x][1])
		self.ax.plot(np.array(xaxle), np.array(yaxle))
		pass
	def displayUsrPoint():
		pass

	# TODO mark points under passed indexes from filepoints as neighbours with black border
	def paintBorders(pointIndexes: list):
		pass

	# TODO mark points under passed indexes from filepoints as neighbours with black border and show distance to usrpoint
	# pass list of lists with: indexes to points that should have border, distance to usrpoint
	def paintBordersWithDistance(pointIndexes: list):
		pass

	# TODO remove border from points
	def removePointBorder():
		pass