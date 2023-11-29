# -*- coding: utf-8 -*-

# Do not run this file, it's library for another python script

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

additionalButtons = False

metrics = ["euklidesowa", "miejska"]
votes = [u"proste", u"ważone odwrotn. kwadratu odległ."]

class Ui_MainWindow(object):
    # Width and height of window. Window can be scaled, but this values are default.
    window_w = 1000
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
        self.__populateGraphLayout()
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout, stretch=2)

        # add graph layout to h layout
        self.graphLayout = QVBoxLayout()
        self.graphLayout.setObjectName(u"graphLayout")
        self.horizontalLayout.addLayout(self.graphLayout, stretch=6)
        pass

    def __populateGraphLayout(self):
        
        # graph
        self.graph = FigureCanvas(Figure(figsize=(5, 3))) # graph
        self.graph.setObjectName(u"graph")
        
        # graph nav menu
        self.graph_nav_menu = NavigationToolbar(self.graph, self.centralwidget)
        self.graph_nav_menu.setObjectName(u"graph_nav_menu")

        self.graphLayout.addWidget(self.graph_nav_menu)
        self.graphLayout.addWidget(self.graph)

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
        self.filelabel.setText(u"📃Plik:\n  " + filepath + u"\n")
        pass
    
    # the element that allows to choose quantity is called spinner, thus name
    def neighbourSpinChanged(self, receiverFunction):
        self.neighbourSpin.valueChanged.connect(receiverFunction)
        #self.neighbourSpin.valueChanged.connect(catchNeighbourSpinChangedExample)
        pass

    def metricChosen(self, receiverFunction):
        self.metricDrop.currentTextChanged.connect(receiverFunction)
        pass

    def votingChosen(self, receiverFunction):
        self.voteDrop.currentTextChanged.connect(receiverFunction)
        pass

    def __populateVLayout(self):
        labelPolicy = QSizePolicy()
        labelPolicy.verticalPolicy = QSizePolicy.Policy.Minimum

        # file button
        self.fileButton = QPushButton(self.centralwidget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setText(u"Wybierz plik")
        self.verticalLayout.addWidget(self.fileButton)

        # file label
        self.filelabel = QLabel(self.centralwidget)
        self.filelabel.setObjectName(u"filelabel")
        self.filelabel.setText(u"📃Plik:\n\tNie wybrano pliku.\n")
        self.filelabel.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.filelabel)

        # neighbours label
        self.neighboursText = QLabel(self.centralwidget)
        self.neighboursText.setObjectName(u"neighboursText")
        self.neighboursText.setText(u"\n🏠🏡K - Ilość sąsiadów:")
        self.neighboursText.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.neighboursText)

        # neighbour spinner
        self.neighbourSpin = QSpinBox(self.centralwidget)
        self.neighbourSpin.setObjectName(u"neighbourSpin")
        self.neighbourSpin.setMinimum(1)
        self.neighbourSpin.setMaximum(20)
        self.verticalLayout.addWidget(self.neighbourSpin)

        # metric label
        self.metricText = QLabel(self.centralwidget)
        self.metricText.setObjectName(u"metricText")
        self.metricText.setText(u"\n📏📐Metryka:")
        self.metricText.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.metricText)

        # metric dropdown
        self.metricDrop = QComboBox(self.centralwidget)
        self.metricDrop.setObjectName(u"metricDrop")
        # metrics = ["euklidesowa", "miejska"]
        # metrics defined on top of file
        self.metricDrop.insertItems(0, metrics)
        self.verticalLayout.addWidget(self.metricDrop)

        # vote label
        self.voteText = QLabel(self.centralwidget)
        self.voteText.setObjectName(u"voteText")
        self.voteText.setText(u"\n🗳📝Rodzaj głosowania:")
        self.voteText.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.voteText)

        # vote dropdown
        self.voteDrop = QComboBox(self.centralwidget)
        self.voteDrop.setObjectName(u"voteDrop")
        # votes = [u"proste", u"ważone odwrotn. kwadratu odległ."]
        # votes defined on top of file
        self.voteDrop.insertItems(0, votes)
        self.verticalLayout.addWidget(self.voteDrop)

        if additionalButtons:
            self.spaceLabel = QLabel(self.centralwidget)
            self.spaceLabel.setObjectName(u"spacingText")
            self.spaceLabel.setText(u"\n")
            self.spaceLabel.setSizePolicy(labelPolicy)
            self.verticalLayout.addWidget(self.spaceLabel)

            # buttons h layout
            self.buttonLayout = QHBoxLayout()
            self.buttonLayout.setObjectName(u"buttonLayout")

            # animate button (in button layout)
            self.animateButton = QPushButton(self.centralwidget)
            self.animateButton.setObjectName(u"animateButton")
            self.animateButton.setText(u"animacja")
            self.buttonLayout.addWidget(self.animateButton)

            # reset button (in button layout)
            self.resetButton = QPushButton(self.centralwidget)
            self.resetButton.setObjectName(u"resetButton")
            self.resetButton.setText(u"reset")
            self.buttonLayout.addWidget(self.resetButton)

            self.verticalLayout.addLayout(self.buttonLayout)

        # widget for spacing
        self.spaceWidget = QWidget(self.centralwidget)
        self.spaceWidget.setObjectName(u"spaceWidget")
        self.verticalLayout.addWidget(self.spaceWidget)

        self.resizeText = QLabel(self.centralwidget)
        self.resizeText.setObjectName(u"resizeText")
        self.resizeText.setText(u"\nOkno można przeskalowywać")
        self.resizeText.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.resizeText)

        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.window_name, None))
    # retranslateUi

def catchNeighbourSpinChangedExample(value):
    print(f"Neighbour spin value is: {value}")