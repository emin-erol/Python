import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglantiOlustur() # Database olusturmak icin kullandik
        self.initUI()
    def baglantiOlustur(self): # Database'imizi olusturup üyeler adında bir tablo olusturduk
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanici_adi TEXT,parola TEXT)")
        baglanti.commit()
    def initUI(self):
        self.IDLabel = QtWidgets.QLabel("ID:")
        self.ID = QtWidgets.QLineEdit()
        self.pwLabel = QtWidgets.QLabel("PW:")
        self.pw = QtWidgets.QLineEdit()
        self.pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.yaziAlani = QtWidgets.QLabel("")
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
        h_box4 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.IDLabel)
        h_box1.addWidget(self.ID)
        h_box1.addStretch()
        h_box2.addStretch()
        h_box2.addWidget(self.pwLabel)
        h_box2.addWidget(self.pw)
        h_box2.addStretch()
        h_box3.addStretch()
        h_box3.addWidget(self.giris)
        h_box3.addStretch()
        h_box4.addStretch()
        h_box4.addWidget(self.yaziAlani)
        h_box4.addStretch()
        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addStretch()
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addLayout(h_box3)
        v_box1.addLayout(h_box4)
        v_box1.addWidget(self.yaziAlani)
        v_box1.addStretch()
        self.setLayout(v_box1)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.Giris)
        self.show()
    def Giris(self):
        kullaniciAdi = self.ID.text() # Inputtan gelen kullanıcı adını ve şifreyi baska degiskenlerde tuttuk
        sifre = self.pw.text()
        # uyeler tablosundaki elemanlarla gönderdiğimiz kullanıcı adı parolayı kıyaslayacagız
        self.cursor.execute("Select * from üyeler where kullanici_adi = ? and parola = ?",(kullaniciAdi,sifre))
        data = self.cursor.fetchall() # data degiskeni eslesme olursa degeri olur olmazsa degeri sıfır olur
        if len(data) == 0:
            self.yaziAlani.setText("Böyle bir kullanıcı adı yok tekrar deneyin.\n")
        else:
            self.yaziAlani.setText("HOŞGELDİNİZ " + kullaniciAdi)

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())