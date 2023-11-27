# This Python file uses the following encoding: utf-8
import sys
import time

import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar # FIXME czy profesor ma te wszystkie pakiety?
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
#import matplotlib.pyplot as plot

from ui_form import Ui_MainWindow

# my imports:
from fileloader import readFile, selectFile
import knn

# Okej, moje UI musi mieć:
# ✔- wybór pliku,
# ✔- graf, menu obsługi grafu
# - (zablokuj edycję grafu!)
# ✔- wybór k [1-20] (liczba sąsiadów)
# ✔- rodzaj metryki - euklidesowa / miejska
# ✔- rodzaj głosowania - proste / ważone odwrotnością kwadratu odległości
# X- ??? lista wyróżnionych sąsiadów i odległości od punktu użytkownika ???
# Na grafie:
# - po wczytaniu cały graf powinien być dobrze widoczny, przeskalowany i wycentrowany
# - kolorowe punkty zależnie od kategorii (6 kategorii [0-5])
# - gdzie użytkownik kliknie to kwadrat, reszta kółka
# - gdy dany punkt jest sąsiadem, należy go wyróżnić np. czarny border
# - obok wyróżnionych punktów podać odległość

class MainWindow(QMainWindow):
    filepoints = []
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.fileButtonClicked(self.getFile)

        # TODO calculations
        knn.graph = self.ui.graph

        # add values to dynamic_canvas
        dynamic_canvas = self.ui.graph # reference to graph canvas, can be edited
        def graph_example(dynamic_canvas):
            self._dynamic_ax = dynamic_canvas.figure.subplots()
            t = np.linspace(0, 10, 101)
            # Set up a Line2D.
            self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
            self._timer = dynamic_canvas.new_timer(50)
            self._timer.add_callback(self._update_canvas_ex)
            self._timer.start()
            pass
        #graph_example(dynamic_canvas)

        #plot.figure(num = dynamic_canvas.figure) # no, cuz this figure is not managed by pyplot

        # TODO initialize GraphManager

        # OK, so create graphs using ax.plot()

    def _update_canvas_ex(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()

    # opens file explorer to select files, then prints file name in window and reads file to filepoints
    def getFile(self): # self or self.ui
        filename = selectFile(self)
        self.ui.displayFilePath(filename)
        self.filepoints = readFile(filename)
        print("filepoints:")
        print(self.filepoints)
        pass


if __name__ == "__main__" or __name__ == "mainwindow": # added or... to allow zadanie1.py execute this file
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


# UI based on example:
# https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html#sphx-glr-gallery-user-interfaces-embedding-in-qt-sgskip-py