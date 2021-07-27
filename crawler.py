import requests
from bs4 import BeautifulSoup 

req = requests.get("https://www.ptt.cc/bbs/movie/index.html") #將此頁面的HTML GET下來
soup=BeautifulSoup(req.text,"html.parser")
sel=soup.select("div.title a")

for s in sel:
    print(s["href"], s.text) 