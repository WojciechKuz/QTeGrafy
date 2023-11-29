

from ui_form import Ui_MainWindow, metrics, votes
from fileloader import readFile, selectFile, normalize
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
        
		# receiver functions should be provided
        self.ui.fileButtonClicked(self.getFile)
        self.ui.neighbourSpinChanged(self.getNofNeighbours)
        self.ui.metricChosen(self.newMetricValue)
        self.ui.votingChosen(self.newVoteValue)
        pass

    # TODO start KNN
    def __startKNN(self):
        pass

	
    # reads file, prints file name in window, reads points and displays it
    def getFile(self): # self or self.ui
        filename = selectFile(self)
        self.ui.displayFilePath(filename)
        self.filepoints = normalize(readFile(filename))
        print(f"nof rows: {len(self.filepoints)}")
        self.graphM.loadPoints(self.filepoints)
        self.graphM.displayPoints()

        # FIXME test area:
        self.graphM.displayUsrPoint(6.3, 4.0)
        #
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
