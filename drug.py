import urllib.request as req
import bs4
import csv


with open('drug.csv','w',newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['產品名稱', '售價'])
    for i in range(5):
        url='https://www.pro-partner.com.tw/ProductBrowse/ProductSubList.aspx?StoreID=1&ParentStoreID=ROOT&CategoryID=L1&ShowFastNewsPage='+str(i)+'&MainMenuID=L&SubMenuID=L1.html'
        request = req.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        })

        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        root = bs4.BeautifulSoup(data, "html.parser")
        items=root.select("div .pro>table")

        for item in items:
            title=item.select("tr>td>span[id^='UcProductSubShow1_MyProductList_Index']")[0].text
            price=item.select("tr>td>span[id^='UcProductSubShow1_MyProductList_SalesPrice_']")[0].text
            csvWriter.writerow([title,price])
            print(title)
            print(price)



