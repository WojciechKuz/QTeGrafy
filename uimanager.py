

from ui_form import Ui_MainWindow
import knn
import graphmanager as gr

# manage ui signals, trigger actions
class UIManager:
    ui: Ui_MainWindow
    graphM: gr.GraphManager
    filepoints = []

    def __init__(self, ui: Ui_MainWindow, graphM: gr.GraphManager):
        self.ui = ui
        self.graphM = graphM
        graphM.setOnPressCall(self.__startKNN) # when usr sets point, calculate knn
        
		# receiver functions should be provided
        #self.ui.fileButtonClicked(self.getFile)
        self.ui.neighbourSpinChanged(self.getNofNeighbours)
        self.ui.metricChosen(self.newMetricValue)
        self.ui.votingChosen(self.newVoteValue)
        pass

    def __getKNNparams(self):
        """Gets values selected in UI by user.
        
        Returns
        -------
        tuple
			Tuple includes: number of neighbours, metric type, voting system
        """
        ui = self.ui
        nofNeighbours = ui.neighbourSpin.value()
        metricType = ui.metricDrop.currentText()
        votingSys = ui.voteDrop.currentText()
        return {
            "nofNeighbours" : nofNeighbours,
            "metricType" : metricType,
            "votingSys" : votingSys
            }

    def __startKNN(self):
        """Calls KNN function"""
        KNNoutput = knn.knn(self.filepoints, self.__getKNNparams(), self.graphM.getusrPointTuple())
        indxList = KNNoutput[0]
        distList = KNNoutput[1]
        colour = KNNoutput[2]
        self.graphM.paintBordersWithDistance(indxList, distList)
        return colour # GraphManager needs this to set user point's colour

	
    # reads points and displays it
    def getPoints(self, points): # self or self.ui
        self.filepoints = points
        print(f"nof rows: {len(self.filepoints)}")
        self.graphM.loadPoints(self.filepoints)
        self.graphM.displayPoints()

        # FIXME test area:
        self.testUI()
        pass

	# Jeśli punkt użytkownika został zaznaczony, to poniższe metody uruchamiają algorytm knn

    def getNofNeighbours(self, k: int):
        if self.graphM.usrpointDefined:
            self.__startKNN
        pass

    def newMetricValue(self, metric: str):
        # proównaj metric z wartościami z metrics
        if self.graphM.usrpointDefined:
            self.__startKNN
        pass

    def newVoteValue(self, voting: str):
        # proównaj voting z wartościami z votes
        if self.graphM.usrpointDefined:
            self.__startKNN
        pass

    def testUI(self): # unfortunately, graph is displayed after completing this method, so sleep call not possible
        #self.graphM.paintBordersWithDistance([14, 3, 67], [14, 3, 69])
        #print("paintBordersWithDistance(...)")
        pass