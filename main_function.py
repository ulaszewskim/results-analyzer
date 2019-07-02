# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import plotly as py
import plotly.graph_objs as go
from os import remove as rm
import os

from LoadCsv import LoadAnswers, LoadKeys
from GetResults import GetResults
from GetKey import GetKey
from ImageFunctions import CropEmptySpace, MergeVertical, MergeHorizontal, ResizeWidth

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

question_images = list(())



results = GetResults(answers, key, all_correct, multiple_sign, pass_rate)


#============
#ALL RESULTS
#============

def TotalResults(results):
    #Information about all results merged
    total_q = len(results[0])-2
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
    
    points=[]
    for a in range(total_q+1):
        points.append(distribution_of_point[a])
    
    #============
    #Chart for all results
    #============
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
    data=[trace1]
    
    if max(points)<10:
        y_dtick = 'auto'
    else:
        y_dtick=None
    
    
    #============
    #layout
    #============
    
    layout = go.Layout(
    #        title=go.layout.Title(
    #            text='Total points',
    #            xref='paper',
    #            x=0.5,
    #            font=dict(
    #                    size=24)
    #            ),
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
    
    py.io.write_image(fig, '_temp_image_chart.png', format='png', width=900, height=500, scale=2)
    CropEmptySpace('_temp_image_chart.png', '_temp_image_chart.png')
    
    
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
                    fill = dict(color='rgb(27, 194, 77)'),
                    font = dict(color='black'),
                    line = dict(color='black')
                    ),
            cells=dict(
                    values = [total_stats[0], total_stats[1]],
                    font = dict(color='black'),
                    line = dict(color='black')
                    ),
            columnwidth=[15,15],
            )
    
    data_t=[table_t]
    fig_t = go.Figure(data=data_t)
    py.io.write_image(fig_t, '_temp_image_table_t.png', format='png', width=500, scale=2)
    CropEmptySpace('_temp_image_table_t.png', '_temp_image_table_t.png')
    

#============
#Deletes temporary files
#============
def DelTemp():
    rm('_temp_image_chart.png')
    rm('_temp_image_table_t.png')


#============
#QUESTIONS
#============
#Information about one question
def OneQuestion(results, answers, question_number):

#    question_number = 1 #START FROM 1
    
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
                    font = dict(color='black'),
                    line = dict(color='black')
                    ),
            cells=dict(
                    values = [question_1[0], question_1[1]],
                    font = dict(color='black'),
                    line = dict(color='black')
                    ),
            columnwidth=[10,10],
            )
    
    
    data=[table_1]
    fig = go.Figure(data=data)
    py.io.write_image(fig, '_temp_image_table1.png', format='png', width=400, scale=2)
    CropEmptySpace('_temp_image_table1.png', '_temp_image_table1.png')
    
    table_2 = go.Table(
            header = dict(
                    values=['<b>Answer</b>', '<b>Number of answers</b>'],
                    fill = dict(color='#a1c3d1'),
                    font = dict(color='black'),
                    line = dict(color='black')
                    ),
            cells=dict(
                    values = [question_2[0], question_2[1]],
                    font = dict(color='black'),
                    line = dict(color='black')
                    ),
            columnwidth=[10,15],
            )
    
    
    
    
    data=[table_2]
    fig = go.Figure(data=data)
    #fig.add_table()
    py.io.write_image(fig, '_temp_image_table2.png', format='png', width=400, scale=2)
    #table_2_image = py.io.to_image(fig, format='png', width=400, scale=2)
    CropEmptySpace('_temp_image_table2.png', '_temp_image_table2.png')
    
    
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
    #        title=go.layout.Title(
    #        text='Question {} - answers'.format(question_number),
    #        xref='paper',
    #        x=0.5,
    #        font=dict(
    #                size=24)
    #        ),
        xaxis = dict(
                linecolor='black',
                mirror=True,
    #            title='Answer',
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
                range = [0,int(max(list(distibution_of_answers.values()))*1.1)]
    #            automargin=True,
    #            dtick = y_dtick
                ),
        )
    
    fig = go.Figure(data=data, layout=layout)
    #fig.add_bar()
    
    
    py.io.write_image(fig, '_temp_image_question.png', format='png', width=450, height=370, scale=2)
    CropEmptySpace('_temp_image_question.png', '_temp_image_question.png')
    
    output_filename = '_question_image{}.png'.format(question_number)
    
    final_question_image = MergeVertical('_temp_image_table1.png', '_temp_image_table2.png', 25)
    final_question_image.save(output_filename)
    final_question_image = MergeHorizontal('_temp_image_question.png',output_filename, 5)
    final_question_image.save(output_filename)
    rm('_temp_image_table1.png')
    rm('_temp_image_table2.png')
    rm('_temp_image_question.png')
    return output_filename

if not os.path.exists('temp'):
    os.makedirs('temp')

def AddQuestionImage(question_images, question_charts):
#    question_images = question_images.sort()
#    question_charts = question_charts.sort()
    
    for z in range(len(question_images)):
        CropEmptySpace(question_images[z], os.path.join('temp', os.path.basename(question_images[z])))
        question_images[z] = os.path.join('temp' , os.path.basename(question_images[z]))
        ResizeWidth(question_images[z],question_images[z],1000)
    for i in range(len(question_charts)):
        
        MergeVertical(question_images[i], question_charts[i], 40).save(question_charts[i])


#TotalResults(results)
question_charts=[]
for q in range(1,7):
    question_charts.append(OneQuestion(results, answers, q))
AddQuestionImage(question_images, question_charts)
#DelTemp()

