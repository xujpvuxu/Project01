import urldata
import re
import bs4
import webbrowser
import time

print("網址範例:http://www.99kubo.tv/vod-read-id-xxxxx.html")
url=input("輸入網址:")
limit=int(input("輸入開始下載的集數:"))
data=urldata.urldatau(url)

xfpall = data.find_all('a', {'href': re.compile('xfplay.html')})

for a in range(len(xfpall)):
    if a >= limit-1: 
        
        urlsec = "https://www.99kubo.tv" + xfpall[a]['href']
        datasec=urldata.urldatau(urlsec)

        xpdata = datasec.find(text=re.compile('dna'))
        regex= re.compile('dna.*?]')
        url=regex.findall(xpdata)
        webbrowser.open("xfplay://"+url[0])
        time.sleep(2)
