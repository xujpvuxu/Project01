import urllib.request


url_pict="https://megapx-assets.dcard.tw/images/8ebedc15-76dc-4a27-92f0-0807583c229e/640.jpeg"
fn = "sexy_pict.jpg"
pict = urllib.request.urlretrieve(url_pict,fn)

##Result:urllib.error.HTTPError: HTTP Error 403: Forbidden