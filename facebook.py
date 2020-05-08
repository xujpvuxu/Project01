import urldata,re
import urllib.request

url=input("網址:")
data=urldata.urldatau(url)

line = data.find(text=re.compile('src_no'))

regex= re.compile('src_no_ratelimit:".*?"')
url= regex.findall(line)

reg = re.compile('".*?"')
url=reg.findall(url[0])

stru=str(url[0]).replace('"','')
urllib.request.urlretrieve(stru,"./FacebookVidwo/FBVideo.mp4")

