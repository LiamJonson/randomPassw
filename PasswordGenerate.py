import random
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)
import sys


num = 0
def genPas(long_pas=8):
    d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '_', '*', '$', '!']
    passw = []
    for i in range(long_pas):
        passw.append(random.choice(d))

    return ''.join(passw)

print(genPas(10))



class MyWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('vvvvvvvvvvvvvvvvvv')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton('&Закрыть')
        self.button = QtWidgets.QPushButton('&Изменить') #///////////
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.button.clicked.connect(self.on_clicked) #//////////////
    def on_clicked(self):                      #///////
            self.label.setText(genPas())  #///////
            self.button.setDisabled(False)          #//////



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Generation Password')
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())




