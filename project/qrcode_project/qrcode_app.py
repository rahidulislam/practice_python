import qrcode
from PIL import Image
import qrcode.constants

# print(dir(qrcode))
data = "https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl"
# img = qrcode.make(data)
# img.save("qrcode.png")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("qrcode1.png")
