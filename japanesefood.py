from urllib.request import urlopen
from bs4 import BeautifulSoup
f=open("japanese food.csv","w")
f.write("評分,日文,英文\n")
for i in range(5):
  print("第",i+1,"頁")
  url="https://tabelog.com/tw/rstLst/"+str(i+1)+"/?lat=35.682955833333004&lon=139.53460666667002&zoom=10&RdoCosTp=2&LstCos=0&LstSitu=0&LstRev=0&LstReserve=0&ChkParking=0&LstSmoking=0&LstCatSD=RC010701&LstCatD=RC0107&LstCat=RC01&Cat=RC"
  response = urlopen(url)
  html = BeautifulSoup(response)
  rs=html.find_all("li",class_="list-rst")
  for r in rs:
    en=r.find("a",class_="list-rst__name-main")
    ja=r.find("small",class_="list-rst__name-ja")
    rating=r.find("b",class_="c-rating__val")
    print(rating.text,ja.text,en.text)
    print(en["href"])
    print("*"*30)
    s="{},{},{}\n".format(rating.text,ja.text,en.text)
    f.write(s)
f.close()
