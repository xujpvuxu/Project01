import urllib.request as req
import urldata

url="https://rate.bot.com.tw/xrt/flcsv/0/day"

req.urlretrieve(url,"每日匯率.csv")

data= open("每日匯率.csv","r",encoding="utf-8")
wdata= open("JPY匯率.txt","w",encoding="utf-8")

for i in range(20):
    line=data.readline()
    if i == 0 :
        global linez
        linez=line.split(",")
     if "JPY" in line:
        linelist = line.split(",")
        for i in range(4):
            wdata.write(linez[i]+":" +linelist[i]+"\n")
data.close()
wdata.close()
            

