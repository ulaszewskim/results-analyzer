# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

from LoadCsv import LoadAnswers, LoadKeys
from GetResults import GetResults
from GetKey import GetKey
from ImageFunctions import CropEmptySpace

exams = [['E.14','X'], ['R.21','X'], ['A.12','X']]

resultsfile='results.csv'

keysfile = 'keys2.csv'

e=0

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
question_number = 2 #START FROM 1

distibution_of_answers= {
        'A':0,
        'B':0,
        'C':0,
        'D':0
}



for a in range(len(answers)):
    q = answers[a][question_number+1]
    if q in distibution_of_answers:
        distibution_of_answers[q]+=1
    else:
        print(a, q)


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

colors = []
for c in range(len(points)):
    if c<pass_rate:
        colors.append('rgb(227, 27, 27)')
    else:
        colors.append('rgb(25, 189, 13)')



trace1 = go.Bar(
        x=list(range(total_q+1)),
        y=points,
        name='Total points',
        text=points,
        textposition='outside',
        textfont=dict(
                size=11,
                color='dimgray'
                ),
        marker=dict(
                color=colors,
                line=dict(
                    color='dimgray',
                    width=1),
                    ),
        )
x=list(range(total_q+1))
data=[trace1]

if max(points)<10:
    y_dtick = 'auto'
else:
    y_dtick=None






#============
#layout
#============

layout = go.Layout(
        title=go.layout.Title(
            text='Total points',
            xref='paper',
            x=0.5,
            font=dict(
                    size=24)
            ),
    xaxis = dict(
            linecolor='black',
            mirror=True,
            title='Points',
            titlefont=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    ),
            dtick=1
            ),
    yaxis = dict(
            linecolor='black',
            mirror=True,
            title='Number of results',
            titlefont=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    ),
            dtick = y_dtick
            ),
    )

fig = go.Figure(data=data, layout=layout)

py.io.write_image(fig, 'chart.png', format='png', width=900, height=500)
CropEmptySpace('chart.png')


#============
#Table for all results
#============

total_stats = [
        ['Questions','Total students', 'Passed', 'Failed'],
        [total_q,len(results), str(how_many_passed)+' ('+str(percent_passed)+'%)', str(len(results)-how_many_passed)+' ('+str(100-percent_passed)+'%)']
        ]

table_t = go.Table(
        header = dict(
                values=['<b>Information</b>', '<b>Value</b>'],
                fill = dict(color='#a1c3d1'),
                ),
        cells=dict(
                values = [total_stats[0], total_stats[1]]),
        columnwidth=[15,15],
        )

data_t=[table_t]
fig_t = go.Figure(data=data_t)
fig_t.add_table()
py.io.write_image(fig_t, 'table.svg', format='svg', width=500)


#============
#Tables for one question
#============

question_1 = [
        ['Question number','Correct answer',],
        [question_number, key[question_number+1]]
        ]


question_2 = [
        ['A', 'B','C','D'],
        [str(distibution_of_answers['A']) + ' (' + str(distibution_of_answers_percent['A'])+'%)',
         str(distibution_of_answers['B']) + ' (' + str(distibution_of_answers_percent['B'])+'%)',
         str(distibution_of_answers['C']) + ' (' + str(distibution_of_answers_percent['C'])+'%)',
         str(distibution_of_answers['D']) + ' (' + str(distibution_of_answers_percent['D'])+'%)']
        ]



table_1 = go.Table(
        header = dict(
                values=['<b>Information</b>', '<b>Value</b>'],
                fill = dict(color='#a1c3d1'),
                ),
        cells=dict(
                values = [question_1[0], question_1[1]],
                ),
        columnwidth=[15,5],
        )


data=[table_1]
fig = go.Figure(data=data)
py.io.write_image(fig, 'table_Q1.png', format='png', width=400)
CropEmptySpace('table_Q1.png')

table_2 = go.Table(
        header = dict(
                values=['<b>Answer</b>', '<b>Number of answers</b>'],
                fill = dict(color='#a1c3d1'),
                ),
        cells=dict(
                values = [question_2[0], question_2[1]],
                ),
        columnwidth=[10,15],
        )




data=[table_2]
fig = go.Figure(data=data)
#fig.add_table()
py.io.write_image(fig, 'table_Q2.png', format='png', width=400)
CropEmptySpace('table_Q2.png')


#============
#Chart for one question
#============

trace2 = go.Bar(
        x=list(distibution_of_answers),
        y=list(distibution_of_answers.values()),
        name='Question {} answers'.format(question_number),
        text=list(distibution_of_answers.values()),
        textposition='outside',
        textfont=dict(
                size=11,
                color='black'),
        marker=dict(
                color='rgb(66, 135, 245)',
                line=dict(
                    color='dimgray',
                    width=1),
            ),
        )


data=[trace2]

layout = go.Layout(
        title=go.layout.Title(
        text='Question {} - answers'.format(question_number),
        xref='paper',
        x=0.5,
        font=dict(
                size=24)
        ),
    xaxis = dict(
            linecolor='black',
            mirror=True,
            title='Answer',
            titlefont=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    ),
            ),
    yaxis = dict(
            linecolor='black',
            mirror=True,
            title='Count',
            titlefont=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    ),
#            automargin=True,
#            dtick = y_dtick
            ),
    )

fig = go.Figure(data=data, layout=layout)
#fig.add_bar()


py.io.write_image(fig, 'question.svg', format='svg', width=900, height=500)
