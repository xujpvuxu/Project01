#!/LouisDing/bin/python3.7
import urllib.request as req #做網路連線
import bs4 #解析網頁
import csv

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
domain='https://rate.bot.com.tw'
request =req.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'})

with req.urlopen(request) as response:
    root = response.read().decode('utf-8')

data = bs4.BeautifulSoup(root,'html.parser')
target=domain + data.select('#ie11andabove > div > div > div > a.btn')[1]['href']

csvdata=req.urlretrieve(target,'data.csv')
with open('data.csv','r',encoding='utf-8') as csvFile:
    with open('text.txt','w',encoding='utf-8') as txtFile:
        csvReader=csv.reader(csvFile)
        listReport=list(csvReader)
        for i in listReport:
            print(i)
            if 'JPY' in i:
               txtFile.write("幣別:" + i[0])
               txtFile.write("\n匯率:" + i[1])
               txtFile.write("\n現金匯率:" + i[2])
               txtFile.write("\n即期匯率:" + i[3])

