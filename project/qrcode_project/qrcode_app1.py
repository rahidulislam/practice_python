import segno

my_qr = segno.make_qr("Hello World")
my_qr.save("qrcode2.png", scale=20, border=10, light="lightblue", dark="darkblue",quiet_zone="red",data_dark="green",data_light="yellow")
