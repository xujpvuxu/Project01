#!/LouisDing/bin/python3.7
#!/李文翔/bin/python3.7
import os
import urllib
from tkinter import *

from urldata import crawler
import time


class App():
    def __init__(self,window):
        #建立變數
        self.urlStr = StringVar()
        self.data = self.urlStr
        self.url=StringVar()
        self.number=0

        #建立Layout
        urlLbl = Label(root, text="網址:", width=8)
        urlLbl.place(x=0, y=5)
        runBtn = Button(root, width=10, text='Run',command=self.download)
        runBtn.place(x=417, y=5)
        self.urlE = Entry(root, width=50, textvariable=self.urlStr)
        self.urlE.place(x=60, y=5)
        self.stateLbl = Label(root, text="等待下載!", width=49,
                              anchor="w", wraplength="350", justify="left",bg="white")
        self.stateLbl.place(x=60, y=40)

    def download(self):
        self.stateLbl.config(text=str("圖片開始下載，請稍候!"), bg="white")
        root.update()
        time.sleep(2)
        # 圖片下載至所屬的資料夾
        dataurl=crawler()
        if not os.path.isdir('.\\提姆img'):
            os.mkdir('.\\提姆img')
            self.stateLbl.config(text=str("圖片開始下載，請稍候!"), bg="white")
        data=dataurl.urldatab(self.urlStr.get())
        self.picurl= data.select('div.mt10 img')
        for count in range(len(self.picurl)):
            img_url=self.picurl[count]['src']
            self.pic=urllib.request.urlretrieve(img_url,"./提姆img/"+str(self.number)+".jpg")
            self.number +=1
        self.stateLbl.config(text=str("下載完成!"), bg="yellow")

if __name__ == '__main__':
    root = Tk()
    root.title('timliao正妹照下載App')
    root.geometry("500x80")
    root.resizable(FALSE, FALSE)
    app = App(root)
    root.mainloop()