# main.py - main class, initializes everything

from PyQt5.QtWidgets import QMainWindow, QPushButton, QBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QIcon
import sys, os
from main.card import Card

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.widget = Card() # make instance of Card() class to enable use
        self.setCentralWidget(self.widget) # set the class widget from another class
        self.setGeometry(50, 50, 320, 300)
        self.setWindowTitle("Oblique Strategies")
        self.setWindowIcon(QIcon(os.path.join('resources', 'logo.png')))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    instance = Main()
    instance.show()
    sys.exit(app.exec_())