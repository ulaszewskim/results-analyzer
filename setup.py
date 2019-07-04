# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd

from GetExamNames import GetExamNames
from LoadCsv import LoadKeys



#================
#Functions
#================
def FillTable(resultsfile, keysfile):
    def ChangeForeground(color):
        examname.config(disabledforeground=color)
        examname.update()
        vers.config(disabledforeground=color)
        vers.update()
        answers_entry.config(disabledforeground=color)
        answers_entry.update()
        final_file.config(disabledforeground=color)
        final_file.update()
        
        
    exams = GetExamNames(resultsfile)
    row=1
    
    global images, total_exams
    total_exams = len(exams)
    
    for i in range(len(exams)):
        images.append(False)
        exam = exams[i]
        
#        chk_var = tk.IntVar()
        chk = tk.Checkbutton(exams_win, command=lambda row=row: Check(row))
        chk.grid(row=row, column=0, pady=2, padx=2)
        
        var_name = tk.StringVar()
        var_name.set(exam[0])
        examname = tk.Entry(exams_win, textvariable=var_name, state='disabled', disabledbackground='gray95', disabledforeground='black', width=25)
        examname.grid(row=row, column=1, pady=2, padx=2)
        
        var_ver = tk.StringVar()
        var_ver.set(exam[1])
        vers = tk.Entry(exams_win, textvariable=var_ver, state='disabled', disabledbackground='gray95', disabledforeground='black', width=10)
        vers.grid(row=row, column=2, pady=2, padx=2)
        
        var_k = tk.StringVar()
        answers_entry = tk.Entry(exams_win, textvariable=var_k, state='disabled', disabledbackground='gray95', disabledforeground='black', width=8)
        answers_entry.grid(row=row, column=3, pady=2, padx=2)
        
        pic_var = tk.StringVar()
        pic_var.set('')
        pictures_entry = tk.Entry(exams_win, textvariable=pic_var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=8)
        pictures_entry.grid(row=row, column=4, pady=2, padx=2)
        
        load_btn = tk.Button(exams_win, text="Load", font=('','8'), width=10, state='disabled', command = lambda row=row: ChooseImagesFiles(row))
        load_btn.grid(row=row, column=5, pady=2, padx=2)
        
        var = tk.StringVar()
        var.set(str(exams[i][0])+'_'+str(exams[i][1]) + '_results.pdf')
        final_file = tk.Entry(exams_win, textvariable=var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=33 )
        final_file.grid(row=row, column=6, pady=2, padx=2)

        bar['value'] = (i+1)*100/len(exams)
        bar.update()
        row+=1
        

    exams_win.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))
    
    select_h.config(state='normal')
    bar['value'] = 0
    bar.update()




def ChangeForeground(row, color):
    examname = exams_win.grid_slaves(row=row, column=1)[0]
    examname.config(disabledforeground=color)
    examname.update()
    vers = exams_win.grid_slaves(row=row, column=2)[0]
    vers.config(disabledforeground=color)
    vers.update()
    answers_en = exams_win.grid_slaves(row=row, column=3)[0]
    answers_en.config(disabledforeground=color)
    answers_en.update()
    pictures = exams_win.grid_slaves(row=row, column=4)[0]
    pictures.config(disabledforeground=color)
    pictures.update()
    resultsfile = exams_win.grid_slaves(row=row, column=6)[0]
    resultsfile.config(disabledforeground=color)
    resultsfile.update()



def FillKeys(keysfile):
    answers = LoadKeys(keysfile)
    for row in range(1,total_exams+1):
        
        chk = exams_win.grid_slaves(row=row, column=0)[0]
        a=chk.configure()['variable'][4]
        b=int(chk.getvar(name=a))
        ans_en = exams_win.grid_slaves(row=row, column=3)[0]
        exam_name = exams_win.grid_slaves(row=row, column=1)[0]
        exam_vers = exams_win.grid_slaves(row=row, column=2)[0]
        exam_name = exam_name.get()
        exam_vers = exam_vers.get()
        
        ChangeForeground(row, 'red')
        chk.config(state='disabled')
        ans_en.config(state='normal')
        ans_en.delete(0, tk.END)
        ans_en.insert(tk.INSERT, 'No Key')
        ans_en.config(state='disabled')
        UncheckRow(row)
        chk.deselect()
        for k in range(len(answers)):
            if answers[k][0] == exam_name and answers[k][1] == exam_vers:
                ChangeForeground(row, 'black')
                ans_en.config(state='normal')
                ans_en.delete(0, tk.END)
                ans_en.insert(tk.INSERT, 'Loaded')
                ans_en.config(state='disabled')
                chk.config(state='normal')
                if b == 1:
                    CheckRow(row)
                    chk.select()
                del answers[k]
                break

        bar['value'] = (row+1)*100/total_exams
        bar.update()
    bar['value'] = 0
    bar.update()

def ChooseResultsFile():
    resultsfile = fd.askopenfilename(filetypes=[('.csv', '*.csv')])
    csv_dir.delete(0, tk.END)
    csv_dir.insert(tk.INSERT, resultsfile)
    FillTable(csv_dir.get(),key_dir.get())
    key_btn.config(state='normal')


def ChooseKeysFile():
    keysfile = fd.askopenfilename(filetypes=[('.csv', '*.csv')])
    key_dir.delete(0, tk.END)
    key_dir.insert(tk.INSERT, keysfile)
    FillKeys(key_dir.get())



def ChooseDestinationFolder():
    destination = fd.askdirectory()
    dst_dir.delete(0, tk.END)
    dst_dir.insert(tk.INSERT, destination)



def ChooseImagesFiles(row):
    imagefiles = fd.askopenfilenames(filetypes=[('Image files', '*.jpg'), ('Image files', '*.png')])
    global images
    images[row-1]=list(imagefiles)
    images[row-1].sort()
    exams_win.grid_slaves(row=row, column=4)[0].config(state='normal')
    exams_win.grid_slaves(row=row, column=4)[0].delete(0, tk.END)
    exams_win.grid_slaves(row=row, column=4)[0].insert(tk.INSERT, len(images[row-1]))
    exams_win.grid_slaves(row=row, column=4)[0].config(state='disabled')


def CheckRow(row):
    examname = exams_win.grid_slaves(row=row, column=1)[0]
    examname.config(disabledbackground='lightgreen')
    examname.update()
    vers = exams_win.grid_slaves(row=row, column=2)[0]
    vers.config(disabledbackground='lightgreen')
    vers.update()
    answers_en = exams_win.grid_slaves(row=row, column=3)[0]
    answers_en.config(disabledbackground='lightgreen')
    answers_en.update()
    pictures = exams_win.grid_slaves(row=row, column=4)[0]
    pictures.config(disabledbackground='lightgreen')
    pictures.update()
    load_btn = exams_win.grid_slaves(row=row, column=5)[0]
    load_btn.config(state='normal', bg='wheat1')
    load_btn.update()
    resultsfile = exams_win.grid_slaves(row=row, column=6)[0]
    resultsfile.config(disabledbackground='lightgreen')
    resultsfile.update()

def UncheckRow(row):
    examname = exams_win.grid_slaves(row=row, column=1)[0]
    examname.config(disabledbackground='grey95')
    examname.update()
    vers = exams_win.grid_slaves(row=row, column=2)[0]
    vers.config(disabledbackground='grey95')
    vers.update()
    answers_en = exams_win.grid_slaves(row=row, column=3)[0]
    answers_en.config(disabledbackground='grey95')
    answers_en.update()
    pictures = exams_win.grid_slaves(row=row, column=4)[0]
    pictures.config(disabledbackground='grey95')
    pictures.update()
    load_btn = exams_win.grid_slaves(row=row, column=5)[0]
    load_btn.config(state='disabled', bg='grey95')
    load_btn.update()
    resultsfile = exams_win.grid_slaves(row=row, column=6)[0]
    resultsfile.config(disabledbackground='grey95')
    resultsfile.update()
    
    
    
def Check(row):
    btn=exams_win.grid_slaves(column=0, row=row)[0]
    a=btn.configure()['variable'][4]
    b=int(btn.getvar(name=a))
    if b==1:
        if btn['state']=='normal':
            CheckRow(row)
    else:
        if btn['state']=='normal':
            UncheckRow(row)



def CheckAll():
    val = select_var.get()

    if val == 0:
        for row in range(1,total_exams+1):
            chk = exams_win.grid_slaves(row=row, column=0)[0]
            if chk['state']=='normal':
                chk.select()
                chk.invoke()
            else:
                chk.deselect()
    else:
        for row in range(1,total_exams+1):
            chk = exams_win.grid_slaves(row=row, column=0)[0]
            chk.deselect()
            chk.invoke()

    






def Start():
    print(images)

#================
#Create global variables
#================
images=[]
total_exams = 0

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
bar = ttk.Progressbar(frame1, length=630, mode='determinate')
bar['value'] = 0
bar.grid(column=0, row=0, columnspan=6, sticky='W', padx=5, pady=5)

#Start button
start_btn = tk.Button(frame1, text='Start', font=('','12'), state='normal', command=Start)
start_btn.grid(column=6, row=0, padx=5, sticky='w')


#Select csv file with results
csv_h = tk.Label(frame1, text = "Select results file:")
csv_h.grid(column=0, row=1, sticky='W', padx=5)

csv_file = tk.StringVar()
csv_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = csv_file)
csv_dir.grid(column=0, row=2, sticky='w', padx=5)

csv_btn = tk.Button(frame1, text = 'Select', command=ChooseResultsFile)
csv_btn.grid(column=1, row=2, sticky='w')


#separator
sep = tk.Label(frame1, text = "")
sep.grid(column=2, row=1, sticky='w', padx=5)


#select key
key_h = tk.Label(frame1, text = "Select correct answers file:")
key_h.grid(column=0, row=3, sticky='w', padx=5, columnspan=3)

key_file = tk.StringVar()
key_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = key_file)
key_dir.grid(column=0, row=4, sticky='w', padx=5)

key_btn = tk.Button(frame1, text = 'Select', command = ChooseKeysFile, state = 'disabled')
key_btn.grid(column=1, row=4, sticky='w')


#separator
sep = tk.Label(frame1, text = "")
sep.grid(column=2, row=4, sticky='w', padx=5)


#Select destination folder
dst_h = tk.Label(frame1, text = "Select destination folder:")
dst_h.grid(column=0, row=5, sticky='w', padx=5)

dst_file = tk.StringVar()
dst_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = dst_file)
dst_dir.grid(column=0, row=6, sticky='w', padx=5)

dst_btn = tk.Button(frame1, text = 'Select', command=ChooseDestinationFolder)
dst_btn.grid(column=1, row=6, sticky='w')


#Input separator when multiple answers
allcor_h = tk.Label(frame1, text = "Multiple separator:")
allcor_h.grid(column=3, row=2, sticky='w')

allcor = tk.StringVar()
allcor_dir = tk.Entry(frame1, width=10, state = 'normal', textvariable = allcor)
allcor_dir.grid(column=4, row=2, sticky='w', padx=2)
'''
#separator
sep = tk.Label(frame1, text = "")
sep.grid(column=2, row=2, sticky='w', padx=5)
'''
#Input sign when all answers are correct
sep_h = tk.Label(frame1, text = "All correct symbol:")
sep_h.grid(column=3, row=4, sticky='w')

sep = tk.StringVar()
sep_dir = tk.Entry(frame1, width=10, state = 'normal', textvariable = sep)
sep_dir.grid(column=4, row=4, sticky='w', padx=2)

#pass rate
pass_rate_h = tk.Label(frame1, text="Pass rate:")
pass_rate_h.grid(column=3, row=6, sticky='W')

pass_r = tk.StringVar()
pass_rate = tk.Entry(frame1, width=10, state='normal', textvariable = pass_r)
pass_rate.grid(column=4, row=6, sticky='W', padx=2)

#pass rate unit
pass_unit = tk.IntVar()
pass_pt = tk.Radiobutton(frame1, text = 'Points', variable = pass_unit, value=1)
pass_pt.grid(column=5, row=6, sticky='W')

pass_per = tk.Radiobutton(frame1, text = '%', variable = pass_unit, value=2)
pass_per.grid(column=6, row=6, sticky='W')

#========
#Exams
#========
frame_canvas = tk.Frame(frame1)
frame_canvas.grid(row=7, column=0, columnspan=100, sticky='news', pady=5, padx=5)
frame_canvas.grid_propagate(True)

canvas = tk.Canvas(frame_canvas, height=580, width=660)
canvas.grid(row=0, column=0, sticky='news')

#scrollbar
vsb = tk.Scrollbar(frame_canvas, orient = 'vertical', command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

exams_win = tk.Frame(canvas, relief='ridge', borderwidth=4)
canvas.create_window((0,0), window=exams_win, anchor='nw')



#headers
select_var = tk.IntVar()
select_h = tk.Checkbutton(exams_win, state='disabled', variable = select_var, command=CheckAll)
select_h.grid(column=0, row=0, sticky='')

exam_h = tk.Label(exams_win, text="Exam", font=('','9','bold'))
exam_h.grid(column=1, row=0, sticky='w')

ver_h = tk.Label(exams_win, text="Version", font=('','9','bold'))
ver_h.grid(column=2, row=0, sticky='w')

answers_h = tk.Label(exams_win, text="Answers", font=('','9','bold'))
answers_h.grid(column=3, row=0, sticky='w')

pictures_h = tk.Label(exams_win, text="Pictures", font=('','9','bold'))
pictures_h.grid(column=4, row=0, sticky='w')

pictures_select_h = tk.Label(exams_win, text="Load", font=('','9','bold'))
pictures_select_h.grid(column=5, row=0)

report_file_h = tk.Label(exams_win, text="New file", font=('','9','bold'))
report_file_h.grid(column=6, row=0, sticky='w')



#scroll options
exams_win.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

window.mainloop()
