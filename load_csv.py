# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import csv


def load_answers(resultsfile, examname):
    """
    Load answers from csv file
    Input examname should be like: [Examname, Version]
    Returns list of lists with uppercased answers to this examname and version
    """
    with open(resultsfile, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        answers = []
        for row in reader:
            if row[0].upper() == examname[0] and row[1].upper() == examname[1]:
                upper_row = [item.upper() for item in row]
                answers.append(upper_row)
    return answers


def load_keys(keysfile):
    """
    Load keys from csv file
    Returns list of lists with uppercased keys
    """
    with open(keysfile, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        keys = list(reader)
        keys_no_empty = []
        for key in keys:
            if key[2] != '':
                keys_no_empty.append(key)
        keys_up = []
        for key in keys_no_empty:
            keys_up.append([item.upper() for item in key])
    return keys_up
