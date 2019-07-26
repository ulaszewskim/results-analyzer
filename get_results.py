# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""


#================

#================
def get_results(answers, key, all_correct, multiple_sign, pass_rate):
    """
    Get results of one exam
    Answers from load_answers
    Key from get_key
    Returns list of results,
    [-2]    total points
    [-1]    pass True/False
    """
    multiple_sign = multiple_sign.upper()
    results = []
    for answer in answers:
        one_result = []
        for i in range(2, len(answers[0])):
            if multiple_sign in key[i]:
                if answer[i]+multiple_sign in key[i] or multiple_sign+answer[i] in key[i]:
                    one_result.append(1)
            elif answer[i] == key[i] or key[i] == all_correct:
                one_result.append(1)
            else:
                one_result.append(0)
        one_result.append(sum(one_result))
        if one_result[-1] >= pass_rate:
            one_result.append(True)
        else:
            one_result.append(False)
        results.append(one_result)
    return results
