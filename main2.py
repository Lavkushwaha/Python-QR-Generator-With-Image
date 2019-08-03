import pyqrcode
from PIL import Image
import datetime

x = datetime.datetime.now()
#id = "BMS123"

def myLoop():
    for i in range(1,500):
        myval = i + 10166
        myAd = "BMS"+str(myval)
        generateQr(str(myAd))

def generateQr(id):
    # Generate the qr code and save as png
    qrobj = pyqrcode.create('http://greenecoindia.com?'+id,)
    with open('test.png', 'wb') as f:
        qrobj.png(f, scale=10,module_color='#13960a')

    # Now open that png image to put the logo
    img = Image.open('test.png')
    img = img.convert("RGBA")

    width, height = img.size

    # How big the logo we want to put in the qr code png
    logo_size = 100

    # Open the logo image
    logo = Image.open('logo.jpg')

    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    #img.show()
    img.save("PNG/"+str(id)+".png", "PNG")

myLoop()