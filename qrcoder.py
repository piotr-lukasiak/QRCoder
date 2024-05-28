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
    imagecoordinates = [0,0]
    pageno = 0
    qrcodecodegroupimage = None 
    for qrcode in qrcodefiles[qrcodefile]:
        qrcode_IMG = write_pil(make_qr(qrcode[0], error='H'),scale = 15, border = 10)
        qrcode_IMG = qrcode_IMG.resize([qr_image_size,qr_image_size], resample = Image.NEAREST)
        draw = ImageDraw.Draw(qrcode_IMG)
        font = ImageFont.truetype(".\\fonts\\FONT.otf", 40)
        textsize1 = draw.textbbox([0, 0],qrcode[1],font=font, align='center')
        textsize2 = draw.textbbox([0, 0],qrcode[2],font=font, align='center')
        draw.text([(qr_image_size-textsize1[2])/2,textsize1[3]+0.08*qr_image_size], qrcode[1], align='center',font=font)
        draw.text([(qr_image_size-textsize2[2])/2,textsize2[3]+0.76*qr_image_size], qrcode[2], align='center',font=font)
        if qrcodecodegroupimage == None:
            qrcodecount = len(qrcodefiles[qrcodefile])
            qrcodecodegroupimage = Image.new("RGBA", size = [2480, 3508] )
            pageno += 1
        if (imagecoordinates[1]+1)*qrcode_IMG.width > 2480:
            imagecoordinates[0] += 1
            imagecoordinates[1] = 0 
        if (imagecoordinates[0]+1)*qrcode_IMG.height > 3508:
            imagecoordinates[0] = 0
            imagecoordinates[1] = 0
            qrcodecodegroupimage.save(qrcodefile +" "+str(pageno) + ".png") 
            qrcodecodegroupimage = Image.new("RGBA", size = [2480, 3508] )
            pageno += 1
        qrcodecodegroupimage.paste(qrcode_IMG, [imagecoordinates[1]*qrcode_IMG.width,imagecoordinates[0]*qrcode_IMG.height])
        imagecoordinates[1] += 1
    qrcodecodegroupimage.save(qrcodefile +" "+str(pageno) + ".png")





