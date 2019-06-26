# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

#================
#Get key to the exam
#Input examname should be like: [Examname, Version]
#Keys from LoadKey
#Returns list, 
#================
def GetKey(keys, exam):
    for a in range(len(keys)):
        if keys[a][0] == exam[0] and keys[a][1] == exam[1]:
            key=keys[a]
            break
    return key