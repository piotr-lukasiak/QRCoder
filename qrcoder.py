import segno
from PIL import Image, ImageDraw
from sys import argv

qrcodefiles = {}

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
    #draw = ImageDraw.Draw(qrcodecodegroupimage)
    for qrcode in qrcodefiles[qrcodefile]:
        qrcode_IMG = segno.make_qr(qrcode[0], error='H').to_pil(scale = 15, border = 15)
        qrcode_IMG = qrcode_IMG.resize([825,825], resample = Image.NEAREST)
        print(imagecoordinates)
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





