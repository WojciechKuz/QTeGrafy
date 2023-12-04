

from ui_form import Ui_MainWindow, metrics, votes
import knn
import graphmanager as gr
import asyncio

# manage ui signals, trigger actions
class UIManager:
    ui: Ui_MainWindow
    graphM: gr.GraphManager
    filepoints = []

    def __init__(self, ui: Ui_MainWindow, graphM: gr.GraphManager):
        self.ui = ui
        self.graphM = graphM
        
		# receiver functions should be provided
        #self.ui.fileButtonClicked(self.getFile)
        self.ui.neighbourSpinChanged(self.getNofNeighbours)
        self.ui.metricChosen(self.newMetricValue)
        self.ui.votingChosen(self.newVoteValue)
        pass

    # TODO start KNN
    def __startKNN(self):
        pass

	
    # reads points and displays it
    def getPoints(self, points): # self or self.ui
        self.filepoints = points
        print(f"nof rows: {len(self.filepoints)}")
        self.graphM.loadPoints(self.filepoints)
        self.graphM.displayPoints()

        # FIXME test area:
        self.testUI()
        pass
    
	# TODO add graph onclick -> display user point

	# TODO Jeśli punkt użytkownika został zaznaczony, to poniższe metody uruchamiają algorytm knn

    def getNofNeighbours(self, k: int):
        pass

    def newMetricValue(self, metric: str):
        # TODO proównaj metric z wartościami z metrics
        pass

    def newVoteValue(self, voting: str):
        # TODO proównaj voting z wartościami z votes
        pass

    def testUI(self): # unfortunately, graph is displayed after completing this method, so sleep call not possible
        #self.graphM.paintBordersWithDistance([14, 3, 67], [14, 3, 69])
        #print("paintBordersWithDistance(...)")
        pass