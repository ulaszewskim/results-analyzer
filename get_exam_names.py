# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import pandas as pd


def get_exam_names(filename):
    """
    get unique exam names
    returns list in format [exam name, version]
    """
    data = pd.read_csv(filename, sep=';', usecols=[0, 1])
    data = data.apply(lambda x: x.astype(str).str.upper())
    exams = data.drop_duplicates()
    exams = exams.sort_values(by=exams.columns[0])
    exams = exams.values.tolist()
    return exams
