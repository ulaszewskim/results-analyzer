# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""


#================
#Get results of one exam
#Answers from load_answers
#Key from get_key
#Returns list of results, 
#   [-2]    total points 
#   [-1]    pass True/False
#================
def get_results(answers, key, all_correct, multiple_sign, pass_rate):
    multiple_sign = multiple_sign.upper()
    results = []
    for s in range(len(answers)):
        one_result = []
        for i in range(2,len(answers[0])):
            if multiple_sign in key[i]:
                if answers[s][i]+multiple_sign in key[i] or multiple_sign+answers[s][i] in key[i]:
                    one_result.append(1)
            elif answers[s][i] == key[i] or key[i] == all_correct:
                one_result.append(1)
            else:
                one_result.append(0)
        one_result.append(sum(one_result))
        if one_result[-1]>=pass_rate:
            one_result.append(True)
        else:
            one_result.append(False)
        results.append(one_result)
    return results
