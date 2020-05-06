import urllib.request as req
import urldata
url="https://rate.bot.com.tw/xrt/flcsv/0/day"

req.urlretrieve(url,"每日匯率.csv")


data= open("每日匯率.csv","r",encoding="utf-8")
wdata= open("JPY匯率.txt","w",encoding="utf-8")

for i in range(20):

    line=data.readline()
    
    if "JPY" in line:
        linelist = line.split(",")
        wdata.write("幣別:"+linelist[0])
        wdata.write("\n匯率:"+linelist[1])
        wdata.write("\n現金匯率:"+linelist[2])
        wdata.write("\n即期匯率:"+linelist[3])

data.close()
wdata.close()
            

