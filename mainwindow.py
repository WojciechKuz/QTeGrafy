import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow, metrics, votes

# FIXME czy profesor ma wszystkie potrzebne pakiety?
# PySide6 (Qt), numpy, matplotlib

# my imports:
from fileloader import *
import graphmanager as gr
import uimanager as uim

# this script can be used as program's entry point

# Okej, moje UI musi mieć:
# ✔- wybór pliku,
# ✔- graf, menu obsługi grafu
# - (zablokuj edycję grafu!)
# ✔- wybór k [1-20] (liczba sąsiadów)
# ✔- rodzaj metryki - euklidesowa / miejska
# ✔- rodzaj głosowania - proste / ważone odwrotnością kwadratu odległości
# X- ??? lista wyróżnionych sąsiadów i odległości od punktu użytkownika ???
# Na grafie:
# ✔- po wczytaniu cały graf powinien być dobrze widoczny, przeskalowany i wycentrowany
# ✔- kolorowe punkty zależnie od kategorii (6 kategorii [0-5])
# - gdzie użytkownik kliknie to kwadrat, reszta kółka
# - gdy dany punkt jest sąsiadem, należy go wyróżnić np. czarny border
# - obok wyróżnionych punktów podać odległość
# - obliczanie knn

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.graph is reference to graph canvas
        self.graphM = gr.GraphManager(self.ui.graph) # initialize GraphManager
        self.uiManager = uim.UIManager(self.ui, self.graphM)
        self.ui.fileButtonClicked(self.getFile)
    
    # reads file, prints file name in window, normalizes data, and passes it to UI manager
    def getFile(self): # self or self.ui
        filename = selectFile(self)
        self.ui.displayFilePath(filename)
        points = normalize(readFile(filename))
        self.uiManager.getPoints(points)
        pass

def checklibs():
    pkgs = ['PySide6', 'matplotlib', 'numpy']
    ihaveall = True
    for p in pkgs:
        try:
            __import__(p)
        except(ImportError):
            print('Nie zainstalowano ', p)
            ihaveall = False
    if not ihaveall:
        print('Nalezy je doinstalowac zeby program dzialal, np. za pomoca pip')
        return False
    return True


if __name__ == "__main__": # file can be renamed to something nicer and still contain this class
    if not checklibs():
        sys.exit(1)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

# UI based on example:
# https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html#sphx-glr-gallery-user-interfaces-embedding-in-qt-sgskip-py