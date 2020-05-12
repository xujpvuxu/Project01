import urldata,re
import webbrowser
url="https://www.dcard.tw/f/sex"

bo=True

maindata=urldata.urldatau(url)
divisaf=maindata.select('a.sc-1v1d5rx-3')
out= open("dcard.txt","w",encoding="utf-8")
for count in range(len(divisaf)):
    if count >=3:
        url="https://www.dcard.tw"+divisaf[count]['href']# 進入分頁
        benchsaf=urldata.urldatau(url)

        pichrefppt = benchsaf.find_all('a',{'href':re.compile('ppt.cc')})
        for a in range(len(pichrefppt)):
            if a == 0 :
                out.write(url+"\n")
                webbrowser.open(url)
                out.write(pichrefppt[a].string+"\n")
                bo=False
            else:
                out.write(pichrefppt[a].string+"\n")

        pichrefrisu = benchsaf.find_all('a',{'href':re.compile('risu')})
        for a in range(len(pichrefrisu)):
            if a == 0 :
                if bo == True:
                    out.write(url+"\n")
                    webbrowser.open(url)
                out.write(pichrefrisu[a].string+"\n")
            else:
                out.write(pichrefrisu[a].string+"\n")
        bo=True
out.close()
                   

# picline = benchsaf.find(text=re.compile('props'))
# regex = re.compile('https://risu.*?')
# match=regex.findall(picline)

