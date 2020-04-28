import urllib.request as req
import bs4


class crawler():
    def urldatau(self, url):
        request = req.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        })

        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        root = bs4.BeautifulSoup(data, "html.parser")

        return root

    def urldatab(self, url):
        request = req.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        })

        with req.urlopen(request) as response:
            data = response.read().decode("BIG5")

        import bs4
        root = bs4.BeautifulSoup(data, "html.parser")

        return root
