import segno
from sys import argv



for argument in argv[1:]:
    qrcounter = 0
    file = open(argument,"r")
    filename = file.name[0:-4]
    qrcodes = file.readlines()
    qrcodes_merged = file.read()
    file.close()
    for code in qrcodes:
        qrcode_IMG = segno.make(code[0:-1], error='H')
        qrcode_IMG.save(code[0:-1] + ".png",scale=4, border= 10)
        qrcounter += 1





