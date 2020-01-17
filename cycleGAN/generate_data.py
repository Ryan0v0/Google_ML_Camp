import PIL
import numpy as np
from PIL import Image, ImageFont
from PIL import ImageDraw
import os


def draw_single_char(font, ch, width, height, path, pos):
    img = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(img)
    draw.text(pos, ch, fill=0, font=font)
    arr = np.array(img)
    arr ^= 255
    # if np.sum(arr) == 0:
    #     return False
    img.save(path)
    return True


def cut_word(path):
    font1 = ImageFont.truetype('kai.ttf', 100)
    font2 = ImageFont.truetype('wxz.ttf', 100)
    with open(path, 'rb') as f:
        s = f.read().decode('utf-8')
        num = 324
        for i in range(len(s)):
            if s[i] == '。' or s[i] == '：' or s[i] == '，' or s[i] == '“' or s[i] == '”' or s[i] == '《' or s[i] == '》' or s[i] == '！' or s[i] == '？' or s[i] == '\n' or s[i] == '\r' or s[i] == '\r\n' or s[i] == ' ' or s[i] == '；' :
                continue
            num += 1
            if not draw_single_char(font1, s[i], 128, 128, 'dataset/train/A/' + '%04d' % (num, ) + '.png', (12, 12)):
                num -= 1
            elif not draw_single_char(font2, s[i], 128, 128, 'dataset/train/B/' + '%04d' % (num,) + '.png', (10, -10)):
                num -= 1
        if num == 1000:
            return


def init():
    path = 'dataset/train/B/'
    for i in range(1, 325):
        img = Image.open(path + '%04d.PNG' % (i, )).convert('L')
        os.remove(path + '%04d.PNG' % (i, ))
        img.resize((128, 128))
        img.save(path + '%04d.png' % (i, ))


if __name__ == '__main__':
    cut_word('ppx.txt')
    # init()
