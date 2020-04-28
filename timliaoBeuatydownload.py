import os
import urllib
from tkinter import *
from tkinter import ttk
import urldata


class App():
    def __init__(self,window):
        #建立變數
        self.urlStr = StringVar()
        self.data = self.urlStr
        #建立Layout
        urlLbl = Label(root, text="網址:", width=8)
        urlLbl.place(x=0, y=5)
        runBtn = Button(root, width=10, text='Run',command=self.download(self.data))
        runBtn.place(x=417, y=5)
        self.urlE = Entry(root, width=50, textvariable=self.urlStr)
        self.urlE.place(x=60, y=5)
        self.stateLbl = Label(root, text="等待下載!", width=49,
                              anchor="w", wraplength="350", justify="left",bg="white")
        self.stateLbl.place(x=60, y=60)

    def download(self,url):
        data=urldata.urldatab(url)
        number=0

        picurl= data.select('div.mt10 img')
        for count in range(len(picurl)):

            pic=urllib.request.urlretrieve(picurl[count]['src'],str(number)+".jpg")
            number +=1

if __name__ == '__main__':
    root = Tk()
    root.title('timliao正妹照下載App')
    root.geometry("500x100")
    root.resizable(FALSE, FALSE)
    app = App(root)
    root.mainloop()