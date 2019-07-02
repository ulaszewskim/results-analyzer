# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

from PIL import Image



#================
#Deletes white borders from image 
#input: path to imagefile
#overwrites inputfile
#================

def CropEmptySpace(imagefile, croppedimage):
    image = Image.open(imagefile)
    cropsize=[image.size[0], image.size[1],0,0]
    w_minmax = []
    h_minmax = []
    for w in range(image.size[0]):
        for h in range(image.size[1]):
            if image.getpixel((w,h)) != (255,255,255,255):
                w_minmax.append(w)
                h_minmax.append(h)
    cropsize=(min(w_minmax), min(h_minmax),max(w_minmax)+1, max(h_minmax)+1)
    image = image.crop(cropsize)
    image.save(croppedimage)


#================
#Merges two images verticaly
#input:
#    image1,image2 - path to imagefiles
#    distance - width of white line separating images [pixels]
#returns image in bytes format
#================

def MergeVertical(image1file, image2file, distance):
    image1 = Image.open(image1file)
    image2 = Image.open(image2file)
    newimage_size = (max(image1.size[0],image2.size[0]), image1.size[1]+image2.size[1]+distance)
    newimage = Image.new('RGB', newimage_size, color=(255,255,255))
    
    area = (0, 0, image1.size[0],image1.size[1])
    newimage.paste(image1, area)
    
    area = (0, image1.size[1]+distance, image2.size[0], image1.size[1] + distance +image2.size[1])
    newimage.paste(image2, area)
    
    return newimage


#================
#Merges two images horizontal
#input:
#    image1,image2 - path to imagefiles
#    distance - width of white line separating images [pixels]
#returns image in bytes format
#================

def MergeHorizontal(image1file, image2file, distance):
    image1 = Image.open(image1file)
    image2 = Image.open(image2file)
    newimage_size = (image1.size[0] + image2.size[0] + distance, max(image1.size[1],image2.size[1]))
    newimage = Image.new('RGB', newimage_size, color=(255,255,255))
    
    area = (0, 0, image1.size[0], image1.size[1])
    newimage.paste(image1, area)
    
    area = (image1.size[0]+distance, 0, image1.size[0] + distance +image2.size[0], image2.size[1])
    newimage.paste(image2, area)
    
    return newimage


#================
#Rezizes image to specific width, keeps aspect ratio
#TO DO: RESIZE AGAIN IF HEIGHT>??
#================
    
def ResizeWidth(imagefile, resizedimage, width):
    image=Image.open(imagefile)
    new_height = width*image.size[1]/image.size[0]
    image.thumbnail((width,new_height), Image.BICUBIC)
    image.save(resizedimage)
    
