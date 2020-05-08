import random
from PyQt5 import QtWidgets, QtCore, QtGui
import sys


def genPas(long_pas=8):
    d = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()-=_?'
    passw = ''.join([random.choice(d) for x in range(long_pas)])
    return ''.join(passw)


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniUi()

    def iniUi(self):
        self.setGeometry(500, 500, 300, 50)
        self.setWindowTitle('Generation Password')
        self.label = QtWidgets.QLabel('Enter value')
        self.labelSize = QtWidgets.QLabel('Size=')
        self.version = QtWidgets.QLabel('v1.05')
        self.version.setAlignment(QtCore.Qt.AlignRight)
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.labelSize.setAlignment(QtCore.Qt.AlignHCenter)

        self.btnQuit = QtWidgets.QPushButton('&Закрыть')
        self.btnclipb = QtWidgets.QPushButton('Copy')

        self.button = QtWidgets.QPushButton('&Generate')
        self.slay = QtWidgets.QSlider(QtCore.Qt.Horizontal)  # Slider
        self.slay.setRange(1, 20)  # Slider
        self.slay.setTickInterval(1)  # Slider
        self.slay.setTickPosition(QtWidgets.QSlider.TicksBelow)  # Slider

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.button, 4, QtCore.Qt.AlignHCenter)
        self.hbox.addWidget(self.btnclipb, 4, QtCore.Qt.AlignHCenter)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addStretch(0)
        self.vbox.addWidget(self.labelSize)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.slay)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.version)

        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.button.clicked.connect(self.on_clicked)
        self.btnclipb.clicked.connect(self.send_to_clipboard)
        self.show()


    def on_clicked(self, *kwarg):
        print('***********')
        self.passw = genPas(int(self.slay.value()))
        self.label.setText(self.passw)
        self.labelSize.setText('Size=' + str(len(self.passw)))
        self.button.setDisabled(False)

    def send_to_clipboard(self,passw):
        passw = self.passw
        cl = QtWidgets.QApplication.clipboard()
        cl.clear(mode=cl. Clipboard)
        cl.setText(passw, mode=cl.Clipboard)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
