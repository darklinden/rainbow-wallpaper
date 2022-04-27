#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import os
import subprocess
import shutil
import sys
import datetime
import errno
import re
import random

from PIL import Image

w = 1170
h = 2532

counts = [8, 7, 7, 7, 8]
colors = [(62, 68, 170, 255), (115, 130, 104, 255),
          (213, 144, 94, 255), (245, 94, 91, 255), (254, 47, 104, 255)]


def make_wallpaper(path):

    newImg = Image.new('RGBA', (w, h), (0, 0, 0, 255))

    total = 0
    for x in counts:
        total += x

    cell_height = math.ceil(h / total)

    start = 0
    offset = 10
    top = start

    for i in range(0, 5):
        print(i)
        c = counts[i]
        color = colors[i]
        for j in range(0, c):
            cell = Image.new('RGBA', (w, cell_height - offset - offset), color)
            newImg.paste(cell, (0, top))
            top += cell_height

    newImg.save(path)


def main():

    cnt = 0

    s_cnt = ('_' + str(cnt)) if cnt > 0 else ''
    name = 'rainbow-wallpaper' + s_cnt + '.png'
    path = os.path.join(os.getcwd(), name)
    while os.path.isfile(path):
        cnt += 1
        s_cnt = ('_' + str(cnt)) if cnt > 0 else ''
        name = 'rainbow-wallpaper' + s_cnt + '.png'
        path = os.path.join(os.getcwd(), name)

    print(path)

    make_wallpaper(path)

    print('Done')


if __name__ == "__main__":
    main()
