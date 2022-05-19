import sys
from PyQt5 import QtWidgets,QtGui

# Horizontal Box, butonların yatayda pencere kenarlarına dayayarak daha efektif kullanmamızı sağlar
# Vertical Box, butonların dikeyde hizalanmasıyla alakalı bir metottur.

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    buton1 = QtWidgets.QPushButton("Giriş")
    buton2 = QtWidgets.QPushButton("Çıkış")
    h_box =QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(buton1)
    h_box.addWidget(buton2)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    """v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(buton1)
    v_box.addWidget(buton2)
    h_box = QtWidgets.QHBoxLayout()
    h_box.addWidget(buton1)
    h_box.addStretch() # Yazıldığı yere göre boşluk bırakır burada ortaya yazıldığı için ortada boşluk olur 
    h_box.addWidget(buton2)"""

    pencere = QtWidgets.QWidget()
    pencere.setLayout(v_box)
    pencere.setWindowTitle("Horizontal ve Vertical Box Layout")
    pencere.setGeometry(300,150,700,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()