import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog,QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from TSNE import tsne
class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        button2 = QPushButton('Process', self)
        button2.setToolTip('This is an example button')
        button2.move(150, 140)
        button2.clicked.connect(self.process)
        self.show()

    def process(self):
        path = self.textbox.text()
        self.ts = tsne(path)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


