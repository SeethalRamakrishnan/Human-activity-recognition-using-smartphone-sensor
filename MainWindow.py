
import sys
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from window import Ui_MainWindow
from TSNE import tsne
from plot import starts


class MainApp:
    def __init__(self):

        self.init_ui()

    def init_ui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

    def init_listeners(self):
        self.ui.pushButtonTSNE.clicked.connect(self.tsne)
        self.ui.pushButtonHist.clicked.connect(self.hist)
    def tsne(self):
        path = self.ui.lineEdit.text()
        print(path)
        self.ts = tsne(path)

    def hist(self):
        path = self.ui.lineEdit.text()
        self.pt = starts(path)
    def start(self):
        self.ui.setupUi(self.MainWindow)
        self.init_listeners()
        self.MainWindow.show()
        sys.exit(self.app.exec_())
if __name__ == '__main__':
    main_app = MainApp()
    main_app.start()
