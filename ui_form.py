# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QVBoxLayout)
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

class Ui_MainWindow(object):
    # Width and height of window. Window can be scaled, but this values are default.
    window_w = 800
    window_h = 600
    window_name = u"QTy graf 🐍" # u for unicode string

    # Get graph via: UI_MainWindowInstance.graph

    def setupUi(self, MainWindow):
        # main window
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(self.window_w, self.window_h)
        # central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        # status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.__populateHLayout()
        self.__populateVLayout()

        self.retranslateUi(MainWindow) # who cares ???

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def __populateHLayout(self):
        # h layout
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        #self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # add v layout to h layout
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)

        # add graph to h layout
        self.graph = FigureCanvas(Figure(figsize=(5, 3))) # graph
        self.graph.setObjectName(u"graph")
        self.horizontalLayout.addWidget(self.graph)
        pass

    def fileButtonClicked(self, receiverFunction):
        self.fileButton.clicked.connect(receiverFunction)
        pass

    def animateButtonClicked(self, receiverFunction):
        self.animateButton.clicked.connect(receiverFunction)
        pass

    def resetButtonClicked(self, receiverFunction):
        self.resetButton.clicked.connect(receiverFunction)
        pass

    def displayFilePath(self, filepath):
        self.filelabel.setText = filepath
        pass
    
    def neighbourSpinChanged(self, receiverFunction):
        self.neighbourSpin.valueChanged.connect(receiverFunction)
        self.neighbourSpin.valueChanged.connect(catchNeighbourSpinChangedExample)
        pass

    def metricChosen(self, receiverFunction):
        self.metricDrop.currentTextChanged.connect(receiverFunction)
        pass

    def votingChosen(self, receiverFunction):
        self.voteDrop.currentTextChanged.connect(receiverFunction)
        pass

    def __populateVLayout(self):

        # file button
        self.fileButton = QPushButton(self.centralwidget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setText(u"Wybierz plik (csv)")
        self.verticalLayout.addWidget(self.fileButton)

        # file label
        self.filelabel = QLabel(self.centralwidget)
        self.filelabel.setObjectName(u"filelabel")
        self.verticalLayout.addWidget(self.filelabel)

        # neighbours label
        self.neighboursText = QLabel(self.centralwidget)
        self.neighboursText.setObjectName(u"neighboursText")
        self.verticalLayout.addWidget(self.neighboursText)

        # neighbour spinner
        self.neighbourSpin = QSpinBox(self.centralwidget)
        self.neighbourSpin.setObjectName(u"neighbourSpin")
        self.verticalLayout.addWidget(self.neighbourSpin)

        # metric label
        self.metricText = QLabel(self.centralwidget)
        self.metricText.setObjectName(u"metricText")
        self.verticalLayout.addWidget(self.metricText)

        # metric dropdown
        self.metricDrop = QComboBox(self.centralwidget)
        self.metricDrop.setObjectName(u"metricDrop")
        self.metrics = ["euklidesowa", "miejska"]
        self.metricDrop.insertItems(0, self.metrics)
        self.verticalLayout.addWidget(self.metricDrop)

        # vote label
        self.voteText = QLabel(self.centralwidget)
        self.voteText.setObjectName(u"voteText")
        self.verticalLayout.addWidget(self.voteText)

        # vote dropdown
        self.voteDrop = QComboBox(self.centralwidget)
        self.voteDrop.setObjectName(u"voteDrop")
        self.votes = [u"proste", u"ważone odwrotn. kwadratu odległ."]
        self.voteDrop.insertItems(0, self.votes)
        self.verticalLayout.addWidget(self.voteDrop)

        # buttons h layout
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")

        # animate button (in button layout)
        self.animateButton = QPushButton(self.centralwidget)
        self.animateButton.setObjectName(u"animateButton")
        self.buttonLayout.addWidget(self.animateButton)

        # reset button (in button layout)
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.buttonLayout.addWidget(self.resetButton)

        self.verticalLayout.addLayout(self.buttonLayout)

        # graph nav menu
        self.graph_nav_menu = NavigationToolbar(self.graph, self.centralwidget)
        self.graph_nav_menu.setObjectName(u"graph_nav_menu")
        self.verticalLayout.addWidget(self.graph_nav_menu)

        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.window_name, None))
    # retranslateUi

def catchNeighbourSpinChangedExample(value):
    print(f"Neighbour spin value is: {value}")