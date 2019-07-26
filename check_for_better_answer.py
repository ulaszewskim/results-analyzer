# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

from operator import itemgetter


def best_min_points(answers, results):
    """
    Get minimum points to be in top 15%
    returns minimum points
    """
    distribution_of_point = {}
    for a in range(len(answers[0])-1):
        distribution_of_point[a] = 0
    for z in range(len(results)):
        index = results[z][-2]
        distribution_of_point[index] += 1
    top_students = int(len(answers)*0.15)
    students = 0
    min_points = len(answers[0])-2
    while students < top_students:
        students = students + distribution_of_point[min_points]
        min_points = min_points-1
    return min_points+1


def check_for_better_answer(min_points, question_number, answers, results, key, multiple_sign, all_correct):
    """
    Check if most of top 15% students answered different than correct answer
    returns list: [True/False, correct_answer, most_answered]
    """
    min_points = best_min_points(answers, results)
    distibution_of_answers_best = {
        'A':0,
        'B':0,
        'C':0,
        'D':0
        }
    correct_answer = key[question_number+1]
    if multiple_sign.upper() in correct_answer or correct_answer == all_correct.upper():
        needs_check = False
        most_answered = all_correct
    else:
        for a in range(len(answers)):
            q = answers[a][question_number+1]
            if q in distibution_of_answers_best and results[a][-2] >= min_points:
                distibution_of_answers_best[q] += 1
        most_answered = max(distibution_of_answers_best.items(), key=itemgetter(1))[0]
        if correct_answer == most_answered:
            needs_check = False
        else:
            needs_check = True
    return [needs_check, correct_answer, most_answered]
