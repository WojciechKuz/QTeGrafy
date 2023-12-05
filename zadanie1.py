import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# czy profesor ma wszystkie potrzebne pakiety?

# this is program's entry point

from mainwindow import *

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

if __name__ == "__main__":
    if not checklibs():
        sys.exit(1)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

