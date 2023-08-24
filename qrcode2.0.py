import pyqrcode 
import png 
from pyqrcode import QRCode 
  

  
  
s = "https://www.udemy.com"
url = pyqrcode.create(s) 
url.svg("udemy.svg", scale = 8) 
url.png('udemy.png', scale = 6) 