from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pyqrcode
import string
import random
from flask import url_for
allchar = string.ascii_letters + string.digits
min_char = 8
max_char = 12


def pass_gen(name, email, payment):
    img = Image.open("app/static/passes/pass.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("app/static/Quicksand-Bold.otf", 32)
    s = "".join(random.choice(allchar)
                for x in range(random.randint(min_char, max_char)))
    s_path = "app/static/passes/" + s + ".png"
    if len(name) >= 18:
        name = name.split()
        name = name[0] + " " + name[1][0]
    seat = str(random.randint(1, 99)) + \
        random.choice(string.ascii_letters).upper()
    draw.text((8, 250), name.upper(), font=font, fill=(255, 255, 255))
    draw.text((397, 250), seat, font=font, fill=(255, 255, 255))
    s1 = "Name:{}\nEmail: {}\nRoom: B-215\n".format(name, email) + \
        "Reach us: http://bit.ly/makebot\nPayment Status: {}".format(
        str(payment))
    dat = pyqrcode.create(s1)
    tp = "app/static/passes/qr_"+s
    dat.png(tp, scale=2)
    img1 = Image.open(tp)
    img.paste(img1, (350, 292))
    img.save(s_path)
    return s+".png"
