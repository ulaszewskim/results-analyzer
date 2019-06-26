# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

from LoadCsv import LoadAnswers, LoadKeys
from GetResults import GetResults
from GetKey import GetKey

exams = [['E.12','X'], ['R.21','X'], ['A.12','X']]

resultsfile='results.csv'

keysfile = 'keys2.csv'

e=1

answers = LoadAnswers(resultsfile, exams[e])
keys = LoadKeys(keysfile)


key = GetKey(keys, exams[e])
all_correct = '1*'
multiple_sign = ' lub '
pass_rate = 21



results = GetResults(answers, key, all_correct, multiple_sign, pass_rate)



#Information about all results merged

how_many_passed=0
for i in range(len(results)):
    if results[i][-1] == True:
        how_many_passed+=1

percent_passed = round(how_many_passed/len(results) *100,2)


distribution_of_point = {}
for a in range(len(answers[0])-2):
    distribution_of_point[a+1]=0

for z in range(len(results)):
    index = results[z][-2]
    distribution_of_point[index] +=1

print('====\nTotal stats:\nTotal students: {}\nPassed: {} students ({}%)\n===='.format(len(results), how_many_passed, percent_passed))


#Information about one question
total_q = len(results[0])-2
question_number = 1 #START FROM 1

distibution_of_answers= {
        'A':0,
        'B':0,
        'C':0,
        'D':0
}



for a in range(len(answers)):
    q = answers[a][question_number+1]
    distibution_of_answers[q]+=1


distibution_of_answers_percent= {
        'A':0,
        'B':0,
        'C':0,
        'D':0
}

distibution_of_answers_percent['A']=round(distibution_of_answers['A']/len(results)*100,2)
distibution_of_answers_percent['B']=round(distibution_of_answers['B']/len(results)*100,2)
distibution_of_answers_percent['C']=round(distibution_of_answers['C']/len(results)*100,2)
distibution_of_answers_percent['D']=round(distibution_of_answers['D']/len(results)*100,2)

print('====\nQuestion {} stats:\nCorrect answer: {}\nA: {} ({}%)\nB: {} ({}%)\nC: {} ({}%)\nD: {} ({}%)\n===='.format(question_number, key[question_number+1],distibution_of_answers['A'], distibution_of_answers_percent['A'], distibution_of_answers['B'], distibution_of_answers_percent['B'], distibution_of_answers['C'], distibution_of_answers_percent['C'], distibution_of_answers['D'], distibution_of_answers_percent['D']))




