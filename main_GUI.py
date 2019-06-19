# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:07:11 2019

@author: Maciej
"""

import tkinter as tk
from tkinter import ttk
from GetExamNames import GetExamNames




#================
#Functions
#================
def FillTable(results, answers):
    exams = GetExamNames(results)
    row=1
    for i in range(len(exams)):
        exam = exams[i]
        
        chk = tk.Checkbutton(exams_win)
        chk.grid(row=row, column=0, pady=2, padx=2)
        
        var = tk.StringVar()
        var.set(exam)
        examname = tk.Entry(exams_win, textvariable=var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=35)
        examname.grid(row=row, column=1, pady=2, padx=2)
        
        var = tk.StringVar()
        var.set('?')
        examname = tk.Entry(exams_win, textvariable=var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=8)
        examname.grid(row=row, column=2, pady=2, padx=2)
        
        var = tk.StringVar()
        var.set('loaded')
        examname = tk.Entry(exams_win, textvariable=var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=8)
        examname.grid(row=row, column=3, pady=2, padx=2)
        
        examname = tk.Button(exams_win, text="Load", font=('','8'), bg='wheat1', width=10)
        examname.grid(row=row, column=4, pady=2, padx=2)
        
        var = tk.StringVar()
        var.set(str(exams[i]) + '_results.docx')
        examname = tk.Entry(exams_win, textvariable=var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=35)
        examname.grid(row=row, column=5, pady=2, padx=2)
        
        row+=1
















#================
#Create main window
#================
window = tk.Tk()
window.title('Results analyzer')
window.geometry('700x800+20+20')


tabControl = ttk.Notebook(window)

frame1=tk.Frame(window,bd=1)
frame1.grid(sticky='news')

tabControl.add(frame1, text = 'Analyzer')
tabControl.grid(column=0,row=0)


frame2=tk.Frame(window)
frame2.grid(sticky='news')

tabControl.add(frame2, text = 'Help')
tabControl.grid(column=1,row=0)


#================
#Frame1 - Analyzer
#================

#Progresbar
bar = ttk.Progressbar(frame1, length=630)
bar['value'] = 0
bar.grid(column=0, row=0, columnspan=6, sticky='W', padx=5, pady=5)

#Start button
start_btn = tk.Button(frame1, text='Start', font=('','12'), state='disabled')
start_btn.grid(column=6, row=0, padx=5, sticky='w')


#Select csv file with results
csv_h = tk.Label(frame1, text = "Select results file:")
csv_h.grid(column=0, row=1, sticky='W', padx=5)

csv_file = tk.StringVar()
csv_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = csv_file)
csv_dir.grid(column=0, row=2, sticky='w', padx=5)

csv_btn = tk.Button(frame1, text = 'Select')
csv_btn.grid(column=1, row=2, sticky='w')


#separator
sep = tk.Label(frame1, text = "")
sep.grid(column=2, row=1, sticky='w', padx=5)


#select key
key_h = tk.Label(frame1, text = "Select correct answers file:")
key_h.grid(column=3, row=1, sticky='w', padx=5, columnspan=3)

key_file = tk.StringVar()
key_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = key_file)
key_dir.grid(column=3, row=2, sticky='w', padx=5, columnspan=3)

key_btn = tk.Button(frame1, text = 'Select')
key_btn.grid(column=6, row=2, sticky='w', padx=7)


#separator
sep = tk.Label(frame1, text = "")
sep.grid(column=2, row=3, sticky='w', padx=5)


#Select destination folder
dst_h = tk.Label(frame1, text = "Select destination folder:")
dst_h.grid(column=0, row=3, sticky='w', padx=5)

dst_file = tk.StringVar()
dst_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = dst_file)
dst_dir.grid(column=0, row=4, sticky='w', padx=5)

dst_btn = tk.Button(frame1, text = 'Select')
dst_btn.grid(column=1, row=4, sticky='w')


#Input separator when multiple answers
allcor_h = tk.Label(frame1, text = "Multiple separator:")
allcor_h.grid(column=5, row=3, sticky='w', padx=5)

allcor = tk.StringVar()
allcor_dir = tk.Entry(frame1, width=15, state = 'normal', textvariable = allcor)
allcor_dir.grid(column=5, row=4, sticky='w', padx=5)

#separator
sep = tk.Label(frame1, text = "")
sep.grid(column=2, row=3, sticky='w', padx=5)

#Input sign when all answersa are correct
sep_h = tk.Label(frame1, text = "All correct symbol:")
sep_h.grid(column=3, row=3, sticky='w', padx=5)

sep = tk.StringVar()
sep_dir = tk.Entry(frame1, width=15, state = 'normal', textvariable = sep)
sep_dir.grid(column=3, row=4, sticky='w', padx=5)

#========
#Exams
#========
frame_canvas = tk.Frame(frame1)
frame_canvas.grid(row=5, column=0, columnspan=100, sticky='news', pady=5, padx=5)
frame_canvas.grid_propagate(True)

canvas = tk.Canvas(frame_canvas, height=630, width=660)
canvas.grid(row=0, column=0, sticky='news')

#scrollbar
vsb = tk.Scrollbar(frame_canvas, orient = 'vertical', command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

exams_win = tk.Frame(canvas, relief='ridge', borderwidth=4)
canvas.create_window((0,0), window=exams_win, anchor='nw')



#headers
select_h = tk.Checkbutton(exams_win)
select_h.grid(column=0, row=0, sticky='')

exam_h = tk.Label(exams_win, text="Exam", font=('','9','bold'), bg='lightblue')
exam_h.grid(column=1, row=0, sticky='w')

answers_h = tk.Label(exams_win, text="Answers", font=('','9','bold'))
answers_h.grid(column=2, row=0, sticky='w')

pictures_h = tk.Label(exams_win, text="Pictures", font=('','9','bold'))
pictures_h.grid(column=3, row=0, sticky='w')

pictures_select_h = tk.Label(exams_win, text="Load", font=('','9','bold'))
pictures_select_h.grid(column=4, row=0)

report_file_h = tk.Label(exams_win, text="New file", font=('','9','bold'))
report_file_h.grid(column=5, row=0, sticky='w')




FillTable('results.csv','keys.csv')


#scroll options
exams_win.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

window.mainloop()