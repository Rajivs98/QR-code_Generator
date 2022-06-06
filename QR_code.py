import qrcode as qr
from PIL import Image, ImageDraw
from qrcode.image.pil import PilImage
from qrcode import image

img = qr.make("https://www.yahoo.com")

img.save("Yahoo.png")
