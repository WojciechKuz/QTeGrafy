import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# FIXME czy profesor ma wszystkie potrzebne pakiety?

# this is program's entry point

from mainwindow import *

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec())

