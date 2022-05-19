import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
htmlIcerigi = response.content
soup = BeautifulSoup(htmlIcerigi,"html.parser")

a = float(input("Rating giriniz: "))
basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for i,j in zip(basliklar,ratingler):
    i = i.text
    j = j.text
    i = i.strip()
    i = i.replace("\n","")
    j = j.strip()
    j = j.replace("\n", "")
    if(float(j) > a):
        print("Başlık: ",i)
        print("Rating: ",j)


