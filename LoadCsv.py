# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import csv

#================
#Load answers from csv file
#Input examname should be like: [Examname, Version]
#Returns list of lists with uppercased answers to this examname and version
#================

def LoadAnswers(resultsfile, examname):
    with open(resultsfile, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        answers = []
        for row in reader:
            if row[0].upper() == examname[0] and row[1].upper() == examname[1]:
                upper_row = [item.upper() for item in row]
                answers.append(upper_row)
    return answers



#================
#Load keys from csv file
#Returns list of lists with uppercased keys
#================

def LoadKeys(keysfile):
    with open(keysfile, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        keys = list(reader)
        keys_no_empty=[]
        for z in range(len(keys)):
            if keys[z][2] != '':
                keys_no_empty.append(keys[z])
        keys_up=[]
        for i in range(len(keys_no_empty)):
            keys_up.append([item.upper() for item in keys_no_empty[i]])
    return keys_up

