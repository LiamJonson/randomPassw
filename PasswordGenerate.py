import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
import sys
from PasGenG import Ui_PasswordGenerator


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PasswordGenerator()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QIcon('simiographics-secure-padlock.ico'))
        self.ui.horizontalSlider.valueChanged.connect(self.gener)
        self.ui.ButtonBuffer.clicked.connect(self.clipboard)
        self.ui.ButtonExit.clicked.connect(self.exit_out)

    def genPas(self, long_pas=8):
        d = '123456789abcdefghigklmnpqrstuvyxwzABCDEFGHIGKLMNPQRSTUVYXWZ!@#$%&*=_?'
        passw = []
        for i in range(long_pas):
            k = random.choice(d)
            if k.islower() not in passw or k.isupper() not in passw or k not in passw:
                passw.append(k)
            else:
                long_pas += 1
        return ''.join(passw)

    def gener(self):
        new_value = self.ui.horizontalSlider.value()
        self.passw = self.genPas(int(new_value))
        self.ui.outputPas.setText(self.passw)
        self.ui.ButtonExit.setDisabled(False)
        print(self.passw)

    def clipboard(self):
        cl = QtWidgets.QApplication.clipboard()
        cl.clear(mode=cl.Clipboard)
        cl.setText(self.passw, mode=cl.Clipboard)
    def exit_out(self):
        self.QCoreApplication.quit()


app = QtWidgets.QApplication(sys.argv)
applic = MyWindow()
applic.show()

sys.exit(app.exec_())
