# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

from operator import itemgetter

#============
#Get minimum points to be in top 15%
#returns minimum points
#============
def BestMinPoints(answers, results):
    
    distribution_of_point = {}
    for a in range(len(answers[0])-1):
        distribution_of_point[a]=0
    
    for z in range(len(results)):
        index = results[z][-2]
        distribution_of_point[index] +=1
    
    top_students = int(len(answers)*0.15)
    
    students = 0
    min_points = len(answers[0])-2
    
    while students<top_students:
        students = students + distribution_of_point[min_points]
        min_points = min_points-1
        
    return min_points+1


#============
#Check if most of top 15% students answered different than correct answer
#returns list: [True/False, correct_answer, most_answered]
#============

def CheckForBetterAnswer(min_points, question_number, answers, results, key):
    distibution_of_answers_best= {
            'A':0,
            'B':0,
            'C':0,
            'D':0
    }
    correct_answer = key[question_number+1]
    
    for a in range(len(answers)):
        q = answers[a][question_number+1]
        if q in distibution_of_answers_best and results[a][-2]>=min_points:
            distibution_of_answers_best[q]+=1
    
    most_answered = max(distibution_of_answers_best.items(), key=itemgetter(1))[0]
    
    if correct_answer == most_answered:
        needs_check = False
    else:
        needs_check = True
    
    return [needs_check, correct_answer, most_answered]