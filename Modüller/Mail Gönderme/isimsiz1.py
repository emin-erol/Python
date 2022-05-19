import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()
message["From"] = "erolemin76@gmail.com"
message["To"] = "zehranuracik@hotmail.com"
message["Subject"] = "Smtp Mail Gönderme"
mesajim = """
    Seni Çok Seviyorum...
    
    Emin EROL
"""
mesaj_govdesi = MIMEText(mesajim,"plain")
message.attach(mesaj_govdesi)
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("erolemin76@gmail.com","ytfcv98.ef")
    mail.sendmail(message["From"],message["To"],message.as_string())
    print("Mail başarıyla gönderildi.")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu.")
    sys.stderr.flush()
