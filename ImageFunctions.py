# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

from PIL import Image


#================
#Deletes white borders from image 
#================

def CropEmptySpace(imagefile):
    image=Image.open(imagefile)
    cropsize=[image.size[0], image.size[1],0,0]
    w_minmax = []
    h_minmax = []
    for w in range(image.size[0]):
        for h in range(image.size[1]):
            if image.getpixel((w,h))!=(255,255,255,255):
                w_minmax.append(w)
                h_minmax.append(h)
    cropsize=(min(w_minmax), min(h_minmax),max(w_minmax)+1, max(h_minmax)+1)
    image=image.crop(cropsize)
    image.save(imagefile)

