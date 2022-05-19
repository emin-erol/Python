import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara" # Verilerini almak istediğimiz internet sitesinin adresi
response = requests.get(url) # Girilen url deki tüm bilgileri alır.
print(response) # Bilgilerin gerçekten alınıp alınmadğını kontrol ettik.
htmlIcerigi = response.content # Sayfanın kod içeriğini aldık
soup = BeautifulSoup(htmlIcerigi,"html.parser") # Kodları parçalayarak daha güzel bir şekilde yazdırmak istedik.
#print(soup.prettify())
for i in soup.find_all("a"):
    print(i)
    print("*"*50)