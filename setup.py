# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter.messagebox as msg
import tkinter.scrolledtext as scrolledtext
import os
from shutil import rmtree
from get_exam_names import get_exam_names
from load_csv import load_keys, load_answers
from get_results import get_results
from get_key import get_key
from create_charts import total_results, one_question
from create_pdf import create_report
from check_for_better_answer import check_for_better_answer



def fill_table(resultsfile):
    """
    Fill table with exam names and versions
    """
    exams = get_exam_names(resultsfile)
    row = 1
    global IMAGES, TOTAL_EXAMS
    TOTAL_EXAMS = len(exams)
    for exam in exams:
        IMAGES.append(False)
        chk = tk.Checkbutton(exams_win, command=lambda row=row: check(row))
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
        load_btn = tk.Button(exams_win, text="Load", font=('', '8'), width=10, state='disabled', command=lambda row=row: choose_images_files(row))
        load_btn.grid(row=row, column=5, pady=2, padx=2)
        var = tk.StringVar()
        var.set(str(exam[0])+'_'+str(exam[1]) + '_results.pdf')
        final_file = tk.Entry(exams_win, textvariable=var, state='disabled', disabledbackground='gray95', disabledforeground='black', width=33)
        final_file.grid(row=row, column=6, pady=2, padx=2)
        bar['value'] = (row+1)*100/len(exams)
        bar.update()
        row += 1
    exams_win.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))
    select_h.config(state='normal')
    bar['value'] = 0
    bar.update()


def change_foreground(row, color):
    """
    Change foreground of specific row
    """
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


def fill_keys(keysfile):
    """
    Fill table with keys info
    """
    answers = load_keys(keysfile)
    for row in range(1, TOTAL_EXAMS+1):
        chk = exams_win.grid_slaves(row=row, column=0)[0]
        a = chk.configure()['variable'][4]
        b = int(chk.getvar(name=a))
        ans_en = exams_win.grid_slaves(row=row, column=3)[0]
        exam_name = exams_win.grid_slaves(row=row, column=1)[0]
        exam_vers = exams_win.grid_slaves(row=row, column=2)[0]
        exam_name = exam_name.get()
        exam_vers = exam_vers.get()
        change_foreground(row, 'red')
        chk.config(state='disabled')
        ans_en.config(state='normal')
        ans_en.delete(0, tk.END)
        ans_en.insert(tk.INSERT, 'No Key')
        ans_en.config(state='disabled')
        uncheck_row(row)
        chk.deselect()
        for answer in answers:
            if answer[0] == exam_name and answer[1] == exam_vers:
                change_foreground(row, 'black')
                ans_en.config(state='normal')
                ans_en.delete(0, tk.END)
                ans_en.insert(tk.INSERT, 'Loaded')
                ans_en.config(state='disabled')
                chk.config(state='normal')
                if b == 1:
                    check_row(row)
                    chk.select()
                del answer
                break
        bar['value'] = (row+1)*100/TOTAL_EXAMS
        bar.update()
    bar['value'] = 0
    bar.update()


def choose_results_file():
    """
    Choose results csv file
    """
    resultsfile = fd.askopenfilename(filetypes=[('.csv', '*.csv')])
    csv_dir.delete(0, tk.END)
    csv_dir.insert(tk.INSERT, resultsfile)
    fill_table(csv_dir.get())
    key_btn.config(state='normal')


def choose_keys_file():
    """
    Choose keys csv file
    """
    keysfile = fd.askopenfilename(filetypes=[('.csv', '*.csv')])
    key_dir.delete(0, tk.END)
    key_dir.insert(tk.INSERT, keysfile)
    fill_keys(key_dir.get())
    dst_btn['state'] = 'normal'


def choose_destination_folder():
    """
    Choose destination directory for the reports
    """
    destination = fd.askdirectory()
    dst_dir.delete(0, tk.END)
    dst_dir.insert(tk.INSERT, destination)
    start_btn['state'] = 'normal'


def choose_images_files(row):
    """
    Choose images to the questions
    """
    imagefiles = fd.askopenfilenames(filetypes=[('Image files', '*.jpg'), ('Image files', '*.png')])
    global IMAGES
    IMAGES[row-1] = list(imagefiles)
    IMAGES[row-1].sort()
    exams_win.grid_slaves(row=row, column=4)[0].config(state='normal')
    exams_win.grid_slaves(row=row, column=4)[0].delete(0, tk.END)
    exams_win.grid_slaves(row=row, column=4)[0].insert(tk.INSERT, len(IMAGES[row-1]))
    exams_win.grid_slaves(row=row, column=4)[0].config(state='disabled')


def check_row(row):
    """
    Changes when row is checked
    """
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


def uncheck_row(row):
    """
    Changes when row is unchecked
    """
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


def check(row):
    """
    Changes state of checkbutton
    """
    btn = exams_win.grid_slaves(column=0, row=row)[0]
    a = btn.configure()['variable'][4]
    b = int(btn.getvar(name=a))
    if b == 1:
        if btn['state'] == 'normal':
            check_row(row)
    else:
        if btn['state'] == 'normal':
            uncheck_row(row)


def check_all():
    """
    Select/unselect all the checkbuttons
    """
    val = select_var.get()
    if val == 0:
        for row in range(1, TOTAL_EXAMS+1):
            chk = exams_win.grid_slaves(row=row, column=0)[0]
            if chk['state'] == 'normal':
                chk.select()
                chk.invoke()
            else:
                chk.deselect()
    else:
        for row in range(1, TOTAL_EXAMS+1):
            chk = exams_win.grid_slaves(row=row, column=0)[0]
            chk.deselect()
            chk.invoke()


def start():
    """
    Start generating reports
    """
    destination = dst_file.get()
    if destination == '':
        msg.showerror('Error', 'Select destination directory')
    if not os.path.exists(destination):
        os.makedirs(destination)
    multiple_sign = multi.get()
    all_correct = allcor.get()
    resultsfile = csv_dir.get()
    keys = load_keys(key_dir.get())
    #get total exams to do to update statusbar
    count = 0
    count_done = 0
    ans = (len(keys[0])-2)*2
    pass_rate = float(pass_r.get())
    for row in range(1, TOTAL_EXAMS+1):
        chk = exams_win.grid_slaves(row=row, column=0)[0]
        a = chk.configure()['variable'][4]
        b = int(chk.getvar(name=a))
        if b == 1:
            count += ans + 1 + 1 + 1 + 1
    if count == 0:
        msg.showerror('Error', 'Select at least one exam')
    #generate reports
    for row in range(1, TOTAL_EXAMS+1):
        chk = exams_win.grid_slaves(row=row, column=0)[0]
        a = chk.configure()['variable'][4]
        b = int(chk.getvar(name=a))
        if b == 1:
            examname = exams_win.grid_slaves(row=row, column=1)[0]
            examname = examname.get()
            version = exams_win.grid_slaves(row=row, column=2)[0]
            version = version.get()
            print('Generating exam {} {} report'.format(examname, version))
            key = get_key(keys, [examname, version])
            answers = load_answers(resultsfile, [examname, version])
            if pass_unit.get() == 2:
                pass_rate = (pass_rate/100)*(len(key)-2)
                print(pass_rate)
            if pass_rate > int(pass_rate):
                pass_rate = int(pass_rate)+1
            else:
                pass_rate = int(pass_rate)
            print(pass_rate)
            count_done += 1
            bar['value'] = (count_done)*100/count
            bar.update()
            print('    Getting results')
            results = get_results(answers, key, all_correct, multiple_sign, pass_rate)
            count_done += 1
            bar['value'] = (count_done)*100/count
            bar.update()
            print('    Creating total charts')
            total_results(results, answers, pass_rate)
            table_t = 'results_temp/_temp_image_table_t.png'
            chart_t = 'results_temp/_temp_image_chart.png'
            charts = []
            b_answers = []
            count_done += 1
            bar['value'] = (count_done)*100/count
            bar.update()
            print('    Creating question charts')
            for c in range(1, len(key)-1):
                charts.append(one_question(results, answers, c, key))
                b_answers.append(check_for_better_answer(pass_rate, c, answers, results, key, multiple_sign, all_correct))
                count_done += 1
                bar['value'] = (count_done)*100/count
                bar.update()
            print('    Generating report...')
            create_report(examname, version, table_t, chart_t, charts, IMAGES[row-1], b_answers, destination)
            count_done += ans/2
            bar['value'] = (count_done)*100/count
            bar.update()
            print('Report {} {} generated'.format(examname, version))
            rmtree('results_temp')
    bar['value'] = 0
    bar.update()
    msg.showinfo('Finished', 'Reports generated successfully')


#================
#Create global variables
#================
IMAGES = []
TOTAL_EXAMS = 0

#================
#Create main window
#================
window = tk.Tk()
window.title('Results Analyzer')
window.geometry('700x700+20+20')
tabControl = ttk.Notebook(window)
frame1 = tk.Frame(window, bd=1)
frame1.grid(sticky='news')
tabControl.add(frame1, text='Analyzer')
tabControl.grid(column=0, row=0)
frame2 = tk.Frame(window, bd=1)
frame2.grid(sticky='news')
tabControl.add(frame2, text='Help')
tabControl.grid(column=1, row=0)

#================
#Frame1 - Analyzer
#================

#Progresbar
bar = ttk.Progressbar(frame1, length=630, mode='determinate')
bar['value'] = 0
bar.grid(column=0, row=0, columnspan=6, sticky='W', padx=5, pady=5)

#Start button
start_btn = tk.Button(frame1, text='Start', font=('', '12'), state='disabled', command=start)
start_btn.grid(column=6, row=0, padx=5, sticky='w')

#Select csv file with results
csv_h = tk.Label(frame1, text="Select results file:")
csv_h.grid(column=0, row=1, sticky='W', padx=5)
csv_file = tk.StringVar()
csv_dir = tk.Entry(frame1, width=43, state='normal', textvariable=csv_file)
csv_dir.grid(column=0, row=2, sticky='w', padx=5)
csv_btn = tk.Button(frame1, text='Select', command=choose_results_file)
csv_btn.grid(column=1, row=2, sticky='w')

#separator
sep = tk.Label(frame1, text="")
sep.grid(column=2, row=1, sticky='w', padx=5)

#select key
key_h = tk.Label(frame1, text="Select correct answers file:")
key_h.grid(column=0, row=3, sticky='w', padx=5, columnspan=3)
key_file = tk.StringVar()
key_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = key_file)
key_dir.grid(column=0, row=4, sticky='w', padx=5)
key_btn = tk.Button(frame1, text = 'Select', command = choose_keys_file, state = 'disabled')
key_btn.grid(column=1, row=4, sticky='w')

#separator
sep = tk.Label(frame1, text="")
sep.grid(column=2, row=4, sticky='w', padx=5)

#Select destination folder
dst_h = tk.Label(frame1, text="Select destination folder:")
dst_h.grid(column=0, row=5, sticky='w', padx=5)
dst_file = tk.StringVar()
dst_dir = tk.Entry(frame1, width=43, state = 'normal', textvariable = dst_file)
dst_dir.grid(column=0, row=6, sticky='w', padx=5)
dst_btn = tk.Button(frame1, state = 'disabled', text = 'Select', command=choose_destination_folder)
dst_btn.grid(column=1, row=6, sticky='w')

#Input separator when multiple answers
multi_h = tk.Label(frame1, text="Multiple separator:")
multi_h.grid(column=3, row=2, sticky='w')
multi = tk.StringVar()
multi_dir = tk.Entry(frame1, width=10, state = 'normal', textvariable = multi)
multi_dir.grid(column=4, row=2, sticky='w', padx=2)
'''
#separator
sep = tk.Label(frame1, text="")
sep.grid(column=2, row=2, sticky='w', padx=5)
'''
#Input sign when all answers are correct
allcor_h = tk.Label(frame1, text="All correct symbol:")
allcor_h.grid(column=3, row=4, sticky='w')
allcor = tk.StringVar()
allcor_dir = tk.Entry(frame1, width=10, state = 'normal', textvariable = allcor)
allcor_dir.grid(column=4, row=4, sticky='w', padx=2)

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
pass_pt.select()
pass_per = tk.Radiobutton(frame1, text = '%', variable = pass_unit, value=2)
pass_per.grid(column=6, row=6, sticky='W')

#========
#Exams
#========
frame_canvas = tk.Frame(frame1)
frame_canvas.grid(row=7, column=0, columnspan=100, sticky='news', pady=5, padx=5)
frame_canvas.grid_propagate(True)
canvas = tk.Canvas(frame_canvas, height=480, width=660)
canvas.grid(row=0, column=0, sticky='news')

#scrollbar
vsb = tk.Scrollbar(frame_canvas, orient = 'vertical', command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)
exams_win = tk.Frame(canvas, relief='ridge', borderwidth=4)
canvas.create_window((0,0), window=exams_win, anchor='nw')

#headers
select_var = tk.IntVar()
select_h = tk.Checkbutton(exams_win, state='disabled', variable = select_var, command=check_all)
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

#================
#Frame2 - Help
#================
links_list = scrolledtext.ScrolledText(frame2, width=96, height=44, font=('',9), state='normal')
links_list.grid(column=0, row=0, sticky='nw')
readme ='author: Maciej Ulaszewski\n\nGeneral information:\nThis software generates charts and tables with data based on exam results. The final PDF file contains both total data and every question data.\n\nAdditional information:\nIt takes 4 different answers: A, B, C, D.\nInformation if majority of 15% of students with best results selected other answer than the correct one.\nPossibility of adding question photo to every question in final report.\n\nSteps:\n1.	Select results data file.\n2.	Select correct answers file.\n3.	Select destination directory for the reports.\n4.	(optional) Fill “Multiple separator” and “All correct symbol”.\n5.	Fill “Pass rate” and select unit.\n6.	Select exams.\n7.	(optional) Load image files\n8.	Start\n\nAdd exam images:\nTo add images use “Load” button in the row with exam. Warning! Names of the image files must be in alphabetical order! If you use numbers to order put zero in front of lower numbers.\nFor example use 01, 02, 03… instead of 1, 2, 3… when number of questions is bigger than 10 and lower than 99.\nIf the question image file’s resolution is too big it will be resized to fit the page.\n\nInput data information:\nInput files are results and keys files in CSV format (separator - ;).\nResults file must contain header, otherwise first row will not be calculated. \nOrder of the results and keys does not matter.\nUppercase/lowercase does not matter.\nIf your answers are not “A/B/C/D” just change it to this.\nIf answer is not A/B/C/D it will be counted as incorrect.\nIt is possible to put multiple correct answers – just fill the “Multiple separator” entry with the separator used in file with\ncorrect answers. For example “ or “ - “A or B or C”.\nAlso when all answers are correct fill the “All correct symbol” entry with the symbol used in file with correct answers.\nThen all answers to this question will be counted as correct. \n\nExample data:\nResults:\nexamname;version;1;2;3;4;5;6;7;8;9;10\nExam3;X;D;D;D;C;C;D;D;B;C;B\nExam1;Y;D;D;A;B;B;D;C;B;B;D\nExam2;X;D;A;D;C;B;B;B;A;C;B\n\nKeys:\nexamname;version;1;2;3;4;5;6;7;8;9;10\nExam1;X;D;B;C;D;B;B;C;C;A;D\nExam2;X;D;all;A;A or B;C;C;C;B;A;D'
links_list.insert(tk.INSERT, readme)
links_list['state'] = 'disabled'
del readme


window.mainloop()
