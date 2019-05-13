import random
from PyQt5 import QtWidgets
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



#app =QtWidgets.QApplication(sys.argv)
#window = QtWidgets.QWidget()
#window.setWindowTitle('Generation Password')
#window.resize(300, 70)
#label = QtWidgets.QLabel(print(genPas(10)))
#btnQuit = QtWidgets.QPushButton('&Закрыть')
#vbox =QtWidgets.QVBoxLayout()
#vbox.addWidget(label)
#vbox.addWidget(btnQuit)
#window.setLayout(vbox)
#btnQuit.clicked.connect(app.quit)
#window.show()
#sys.exit(app.exec_())