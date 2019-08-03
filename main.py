import pyqrcode
from PIL import Image
# import urllib.urlencode
# params = {'q': 'Python 2.x URL encoding', 'as_sitesearch': 'www.urlencoder.io'}
# myurl = urllib.urlencode(params)
url = pyqrcode.QRCode('http://greenecoindia.com?BMS123',error = 'H')
url.png('test.png',scale=10)
im = Image.open('test.png')
im = im.convert("RGBA")
logo = Image.open('logo.jpg')
box = (135,135,235,235)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.show()