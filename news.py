import urldata
import re
import webbrowser

url="https://www.facebook.com/news.ebc/videos/925576217862677"
data=urldata.urldatau(url)

needline=data.find(text=re.compile('src_no'))

regex=re.compile('src_no_ratelimit:".*?"')
match= regex.findall(needline)

reg=re.compile('https.*')
mat=reg.findall(match[0])

strmat=str(mat[0])
matc=strmat.replace("\"","")

print(matc)

webbrowser.open(matc)





