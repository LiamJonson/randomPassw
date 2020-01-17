import random
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
   QInputDialog, QApplication)
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
import sys
num = 0
def genPas(long_pas=8):
   d = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()-=_?'
   passw = ''.join([random.choice(d) for x in range(long_pas)])
   return ''.join(passw)

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
       super().__init__()
       self.iniUi()
    def iniUi(self):
       self.setWindowTitle('Generation Password')
       self.label = QtWidgets.QLabel('нет значения')
       self.version = QtWidgets.QLabel('v1.02')
       self.version.setAlignment(QtCore.Qt.AlignRight)
       self.label.setAlignment(QtCore.Qt.AlignHCenter)
       self.btnQuit = QtWidgets.QPushButton('&Закрыть')
       self.button = QtWidgets.QPushButton('&Изменить') #///////////
       self.butAlter = QtWidgets.QSpinBox()
       self.vbox = QtWidgets.QVBoxLayout()
       self.vbox.addWidget(self.label)
       self.vbox.addWidget(self.butAlter)
       self.vbox.addWidget(self.button)
       #self.vbox.addWidget(self.btnQuit) #buttonExit
       self.vbox.addWidget(self.version)
       self.setLayout(self.vbox)
       self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
       self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
       self.p = self.butAlter.text()
       self.label.setText(genPas(int(self.p)))#////////////
       self.button.setDisabled(False)          #//////
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   window = MyWindow()
   window.resize(300, 50)
   window.show()
   sys.exit(app.exec_())

