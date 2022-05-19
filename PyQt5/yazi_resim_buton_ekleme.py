import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ilk Uygulama")
    pencere.setGeometry(0,0,1920,1080)
    label1 = QtWidgets.QLabel(pencere)
    label1.setText("HOŞGELDİNİZ")
    label1.move(1700,100)
    label2 = QtWidgets.QLabel(pencere)
    label2.setPixmap(QtGui.QPixmap("doga.png"))
    button1 = QtWidgets.QPushButton(pencere)
    button1.setText("GİRİŞ")
    button1.move(1700,200)
    pencere.show()
    sys.exit(app.exec_())

Pencere()