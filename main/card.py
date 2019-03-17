#!python3.7.2
# card.py - class for the oblique strategy itself

from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys, random, os

class Card(QWidget):
    
    def __init__(self):
        super().__init__()


        self.button = QPushButton("Stuck? Click me!")
        self.layout = QVBoxLayout()

        self.button.setStyleSheet("QPushButton {font-size: 10; font-family: consolas;}")
        self.button.clicked.connect(self.on_click)

        self.font = QFont("Consolas", 20, QFont.Bold)
        self.strategy = QLabel("Click the button for a strategy")
        self.strategy.setFont(self.font)
        self.strategy.setAlignment(Qt.AlignCenter)
        self.strategy.setWordWrap(True)



        self.layout.addWidget(self.strategy)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout) # set the qvboxlayout to qwidget

        self.oblique()


    def oblique(self):
        self.obliqueStrategies = open(os.path.join('resources', 'obliqueStrategies.txt'), 'r') # locate the file, no matter the OS -- up a level -> dependecies -> obliqueStrategies.txt
        self.lines = self.obliqueStrategies.readlines()

        self.obliqueStrategies.seek(0) # go back to first byte to prepare for next line
        self.numOfLines = len(self.obliqueStrategies.readlines()) # variable to use for random, reads how many lines

    @pyqtSlot()
    def on_click(self):
        self.dialog = self.lines[random.randint(0, (self.numOfLines - 1))] # assign the string that would be acquired here to dialog

        self.strategy.setText(self.dialog) # set label to the string of dialog


