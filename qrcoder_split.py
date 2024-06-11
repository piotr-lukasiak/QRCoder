from segno import make_qr
from segno_pil import write_pil
from PIL import Image, ImageDraw, ImageFont
from sys import argv

qrcodefiles = {}
qr_image_size = 600

for argument in argv[1:]:
    qrcounter = 0
    file = open(argument,"r")
    filename = file.name[0:-4]
    qrcodefiles[filename] = [str(x).strip().split(",") for x in file.readlines()]
    file.close()

for qrcodefile in qrcodefiles:
    imno = 0
    for qrcode in qrcodefiles[qrcodefile]:
        qrcode_IMG = write_pil(make_qr(qrcode[0], error='H'),scale = 15, border = 10)
        qrcode_IMG = qrcode_IMG.resize([qr_image_size,qr_image_size], resample = Image.NEAREST)
        draw = ImageDraw.Draw(qrcode_IMG)
        font = ImageFont.truetype(".\\fonts\\FONT.otf", 40)
        textsize1 = draw.textbbox([0, 0],qrcode[1],font=font, align='center')
        textsize2 = draw.textbbox([0, 0],qrcode[2],font=font, align='center')
        draw.text([(qr_image_size-textsize1[2])/2,textsize1[3]+0.08*qr_image_size], qrcode[1], align='center',font=font)
        draw.text([(qr_image_size-textsize2[2])/2,textsize2[3]+0.76*qr_image_size], qrcode[2], align='center',font=font)
        qrcode_IMG.save(qrcodefile+str(imno) + ".png")
        imno += 1





