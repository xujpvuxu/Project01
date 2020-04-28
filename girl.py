import urldata
import urllib.request

def download(url):
    data=urldata.urldatab(url)
    number=0

    picurl= data.select('div.mt10 img')
    for count in range(len(picurl)):
        pic=urllib.request.urlretrieve(picurl[count]['src'],str(number)+".jpg")
        number +=1
