
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.markers import MarkerStyle
from matplotlib.backends.backend_qtagg import FigureCanvas # ???
from numpy import array as nparray

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
	"""GraphManager:
	Draws graph after loading and after onClick for KNN.
	
	Initializing:
	- GraphManager()
	- loadPoints()
	- setOnPressCall()

	When GraphManager is initialized (all methods above had been executed)
	then when onClick is detected graph is redrawn.
	When function/method provided to setOnPressCall()
	is called, then after calculating KNN, it should call drawGraph().
	"""
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

	def setOnPressCall(self, onPressCall):
		"""
		Params
		------
		onPressCall: function
		"""
		self.onPressCall: function = onPressCall
		pass

	def displayPoints(self):
		self.ax.clear()
		self.ax.scatter(nparray(self.xaxle), nparray(self.yaxle), c=self.pointcool, edgecolors=self.bordercool, marker='o')
		if self.usrpointDefined:
			xarr = nparray([self.usrpoint[0]])
			yarr = nparray([self.usrpoint[1]])
			self.ax.scatter(xarr, yarr, c=colours.get(self.usrpoint[2], "grey"), edgecolors="none", marker="s")
		self.draw()
		self.tight()
		pass

	def on_press(self, event):
		# print("Event:")
		# print(f"\tx: {event.x}, y: {event.y}")
		# print(f"\txdata: {event.xdata}, ydata: {event.ydata}")
		if hasattr(self, "onPressCall"):
			self.onPressCall((event.xdata, event.ydata)) # onPressCall is set in UIManager, calls __startKNN()
		else:
			print("Error, you have to setOnPressCall() before calling on_press()")
		pass

	def getusrPointTuple(self) -> tuple:
		"""
		Returns
		-------
		tuple(float, float)"""
		return (self.usrpoint[0], self.usrpoint[1])

	def setUsrPointT(self, xy: tuple, col: int):
		self.setUsrPoint(xy[0], xy[1], col)
		pass

	def setUsrPoint(self, x: float, y: float, col: int):
		if not self.usrpointDefined:
			self.usrpointDefined = True
			self.usrpoint = [x, y, col, "none", 's']
		else:
			self.usrpoint[0] = x
			self.usrpoint[1] = y
			self.usrpoint[2] = col
		pass
	

	# mark points under passed indexes from filepoints as neighbours with black border
	def setBorders(self, pointIndexes: list):
		for i in pointIndexes:
			self.bordercool[i] = "black"
		pass

	def annotatePoints(self, indexesAndDistances: list):
		offset = 0.02
		for iandd in indexesAndDistances:
			indx = iandd[0]
			xy = (self.xaxle[indx], self.yaxle[indx]) # point position
			xytxt = (self.xaxle[indx] + offset, self.yaxle[indx] + offset) # annotation position 
			txt = iandd[1] # annotation text
			self.bordercool[indx] = "black"
			self.ax.annotate(txt, xy, xytxt)
		pass

	# remove border from points
	def resetBordercool(self):
		for i in range(len(self.bordercool)): # I probably just commited Python war-crime
			self.bordercool[i] = "none"
		pass

	def drawGraph(self, indxAndDistList: list, usrpoint: tuple, colour: int):
		"""All-in-one graph drawing function"""
		self.setUsrPointT(usrpoint, colour)
		self.setBorders([x[0] for x in indxAndDistList])
		self.displayPoints()
		self.annotatePoints(indxAndDistList)
		self.resetBordercool()
		pass