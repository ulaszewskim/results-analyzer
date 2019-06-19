# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:07:45 2019

@author: Maciej
"""

import pandas as pd

#================
#Get unique exam names
#Returns list
#================

def GetExamNames(filename):
    data = pd.read_csv(filename, sep=';', usecols=[0])
    #get unique values
    exams = data[data.columns.values.tolist()[0]].unique().tolist()
    #uppercase all results
    for i in range(len(exams)):
        exams[i]=exams[i].upper()
    #remove duplicates
    exams=list(set(exams))
    exams.sort()
    return exams
