import urldata
import re
import bs4
import webbrowser
import time
url = "http://www.99kubo.tv/vod-read-id-95768.html"#url
data=urldata.urldatau(url)

xfpall = data.find_all('a', {'href': re.compile('sid-1-pid')})#sid-1-pid會變動
for a in range(len(xfpall)):
    if a >= 126:  #要取的集數-1
        urlsec = "https://www.99kubo.tv" + a['href']
        datasec=urldata.urldatau(urlsec)

        xpdata = datasec.find(text=re.compile('dna'))
        regex= re.compile('dna.*?]')
        url=regex.findall(xpdata)
        webbrowser.open("xfplay://"+url[0])
        time.sleep(5)
        b+=1



