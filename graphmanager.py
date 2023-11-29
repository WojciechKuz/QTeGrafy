
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.backends.backend_qtagg import FigureCanvas # ???
import numpy as np

colours = {
	0: "blue",
	1: "cyan",
	2: "#0f0",
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
	usrpoint: tuple # as x, y, colour. -1 = colour not found yet
	def loadPoints(self, points):
		self.__points = points

	def displayPoints(self):
		self.xaxle = [] # TODO make it class member and editable, so paint porders would only change points that need it, and not create all again
		self.yaxle = []
		self.pointcool = [] # colours
		self.bordercool = [] # border colour
		for x in self.__points: # points is list of tuples(float, float, int) so x is tuple(float, float, int) 
			self.xaxle.append(x[0])
			self.yaxle.append(x[1])
			self.pointcool.append(colours.get(x[2], "grey")) # in case, grey colour marks errors
			self.bordercool.append("none")
		self.ax.scatter(np.array(self.xaxle), np.array(self.yaxle), c=self.pointcool, edgecolors=self.bordercool)
		pass

	def displayUsrPoint(self):
		self.__refreshView()
		self.ax.plot(np.array([6.3]), np.array([4.0]), marker="s")
		pass

	# mark points under passed indexes from filepoints as neighbours with black border
	def paintBorders(self, pointIndexes: list):
		for i in pointIndexes:
			self.bordercool[i] = "black"
		self.__refreshView()
		pass

	# TODO mark points under passed indexes from filepoints as neighbours with black border and show distance to usrpoint
	# pass list of tuples with: indexes to points that should have border, distance to usrpoint
	def paintBordersWithDistance(self, pointIndexes: list):
		pass

	# remove border from points
	def removePointBorder(self):
		for i in range(len(self.bordercool)): # I probably just commited Python war-crime
			self.bordercool[i] = "none"
		self.__refreshView()
		pass

	def __refreshView(self):
		self.ax.clear()
		self.ax.scatter(np.array(self.xaxle), np.array(self.yaxle), c=self.pointcool, edgecolors=self.bordercool)