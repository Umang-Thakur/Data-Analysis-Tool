from numpy.lib.function_base import select

from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

import pandas as pd
import pdfkit as pdf
import time


class Main(Ui_MainWindow):
    def __init__(self):
        super.__init__()

    def train(self):
        self.model.fit(self.x, self.y)
        out = self.model.predict(self.x)
        print(out)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())