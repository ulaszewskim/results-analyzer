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

e=2

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
for a in range(len(answers[0])-1):
    distribution_of_point[a]=0

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





#============
#Chart for all results
#============


import plotly as py
import plotly.graph_objs as go



points=[]
for a in range(total_q+1):
    points.append(distribution_of_point[a])



trace1 = go.Bar(
        x=list(range(total_q+1)),
        y=points,
        name='Total points',
        text=points,
        textposition='outside',
        textfont=dict(
                size=9,
                color='dimgray'),
        marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1),
            ),
        )
x=list(range(total_q+1))
data=[trace1]

if max(points)<10:
    y_dtick = 'auto'
else:
    y_dtick=None

layout = go.Layout(
        title=go.layout.Title(
        text='Total points',
        xref='paper',
        x=0.5,
        font=dict(
                size=24)
        ),
    xaxis = dict(
            title='Points',
            titlefont=dict(
                    family='Arial',
                    size=18,
                    color='black'
                    ),
            dtick=1
            ),
    yaxis = dict(
            title='Number of results',
            titlefont=dict(
                    family='Arial',
                    size=18,
                    color='black'
                    ),
            dtick = y_dtick
            ),
    shapes = [dict(
            type='line',
            x0=pass_rate-0.5,
            y0=0,
            x1=pass_rate-0.5,
            y1=max(points),
            line= dict(
                color= 'lightgreen',
                width= 2,
                )
            )]
    )

fig = go.Figure(data=data, layout=layout)
fig.add_bar()


py.io.write_image(fig, 'chart.png', format='png', width=1000, height=500)

