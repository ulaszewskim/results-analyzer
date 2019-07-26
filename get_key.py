# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""


def get_key(keys, exam):
    """
    Get key to the exam
    Input examname should be like: [Examname, Version]
    Keys from load_keys
    Returns list,
    """
    for one_key in keys:
        if one_key[0] == exam[0] and one_key[1] == exam[1]:
            key = one_key
            break
    return key
