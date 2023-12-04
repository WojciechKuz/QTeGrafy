
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.markers import MarkerStyle
from matplotlib.backends.backend_qtagg import FigureCanvas # ???
import numpy as np

colours = {
	0: "blue",
	1: "cyan",
	2: "#0f0",
	3: "orange",
	4: "red",
	5: "magenta",
	229: "#229"
}

class GraphManager:
	ax: Axes
	usrpoint: list # as x, y, colour, border, marker. list, because I need this to be mutable
	usrpointDefined = False

	def __init__(self, figcanv: FigureCanvas):
		fig: Figure = figcanv.figure
		self.ax = fig.subplots()
		self.cidpress = fig.canvas.mpl_connect('button_press_event', self.on_press) # has to keep reference
		self.draw: function = fig.canvas.draw # reference to method for redrawing graph
		self.tight: function = fig.tight_layout # makes graph take more space that would be empty otherwise
		# Alternatively to draw, I could have programatically press home button on graph toolbar

		# create graphs using ax.plot() or ax.scatter()
		pass


	# 'points' should be list of tuples(float, float, int) filepoints
	def loadPoints(self, points):
		self.xaxle = []
		self.yaxle = []
		self.pointcool = [] # colours
		self.bordercool = [] # border colour
		for x in points:
			self.xaxle.append(x[0])
			self.yaxle.append(x[1])
			self.pointcool.append(colours.get(x[2], "grey")) # in case, grey colour marks errors
			self.bordercool.append("none")
		pass

	def displayPoints(self):
		self.ax.clear()
		self.ax.scatter(np.array(self.xaxle), np.array(self.yaxle), c=self.pointcool, edgecolors=self.bordercool, marker='o')
		if self.usrpointDefined:
			xarr = np.array([self.usrpoint[0]])
			yarr = np.array([self.usrpoint[1]])
			self.ax.scatter(xarr, yarr, c=colours.get(self.usrpoint[2], "grey"), edgecolors="none", marker="s")
		self.draw()
		self.tight()

	def on_press(self, event):
		# print("Event:")
		# print(f"\tx: {event.x}, y: {event.y}")
		# print(f"\txdata: {event.xdata}, ydata: {event.ydata}")
		self.displayUsrPoint(event.xdata, event.ydata)
		pass

	def displayUsrPoint(self, x: float, y: float):
		if not self.usrpointDefined:
			self.usrpointDefined = True
			self.usrpoint = [x, y, 229, "none", 's']
		else:
			self.usrpoint[0] = x
			self.usrpoint[1] = y
		self.displayPoints()
		pass

	# mark points under passed indexes from filepoints as neighbours with black border
	def paintBorders(self, pointIndexes: list):
		for i in pointIndexes:
			self.bordercool[i] = "black"
		self.displayPoints()
		pass

	# mark points under passed indexes from filepoints as neighbours with black border and show distance to usrpoint
	# pass list of tuples with: indexes to points that should have border (that are neighbours), distance of them to usrpoint
	def paintBordersWithDistance(self, pointIndexes: list, pointDistance: list):
		nofp = len(pointIndexes)
		if len(pointDistance) != nofp:
			raise Exception(f"Different number of elements in pointIndexes ({nofp}) and in  pointDistance ({len(pointDistance)})")
		self.paintBorders(pointIndexes)
		offset = 0.02
		for i in range(nofp): # can't be for i in pointIndexes, because I operate on two lists
			indx = pointIndexes[i]
			xy = (self.xaxle[indx], self.yaxle[indx]) # point position
			xytxt = (self.xaxle[indx] + offset, self.yaxle[indx] + offset) # annotation position 
			txt = pointDistance[i] # annotation text
			self.bordercool[indx] = "black"
			self.ax.annotate(txt, xy, xytxt)
		pass

	# remove border from points
	def removePointBorder(self):
		for i in range(len(self.bordercool)): # I probably just commited Python war-crime
			self.bordercool[i] = "none"
		self.displayPoints()
		pass