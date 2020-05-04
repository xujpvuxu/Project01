import urldata
import re
import webbrowser
import time

url = input("輸入網址")
num=input("第幾集開始下載")

data=urldata.urldatau(url)

fdurl=data.find('a',{'href': re.compile('download.php')})
url="http://www.99kubo.tv"+fdurl['href']

data=urldata.urldatau(url)
du = data.select('div.media a')
if num == "":
    num =len(du)

for a in range(len(du)):
    if a>= int(num)-1:
        webbrowser.open(du[a]['href'])
        time.sleep(2)
    
#webbrowser.open(du['href'])
#print(du['href'])



