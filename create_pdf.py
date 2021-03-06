# -*- coding: utf-8 -*-
"""
@author: Maciej Ulaszewski
mail:ulaszewski.maciej@gmail.com
github: https://github.com/ulaszewskim
"""

import os
from fpdf import FPDF
from PIL import Image


class PDF(FPDF):
    def header(self):
        if self.page_no() != 1:
            self.set_font('Arial', size=6)
            self.set_text_color(128)
            self.cell(0, 4, 'Generated using Results Analyzer, author: Maciej Ulaszewski', 0)
            self.ln(7)

    def footer(self):
        if self.page_no() != 1:
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def question_title(self, num):
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.set_fill_color(196, 215, 245)
        self.cell(0, 6, 'Question {}'.format(num), 0, 1, 'L', 1)
        self.ln(3)

    def question_body(self, question_image, chart, better_answer, width):
        self.set_font('Times', '', 12)
        if question_image != False:
            self.image(question_image, w=width)
            self.ln(3)
        self.image(chart, w=175)
        if better_answer[0]:
            self.ln(5)
            self.set_font('Arial', size=10)
            self.set_text_color(255, 0, 0)
            self.cell(0, 4, 'Correct answer is {}, while most of best students picked {}'.format(better_answer[1], better_answer[2]), 0)
        self.ln(10)

    def print_question(self, num, question_image, chart, better_answer):
        print('        Printing question {}'.format(num))
        position = self.get_y()
        width = None
        quest_h = 0
        if question_image != False:
            const = 0.0836
            c_w = 1
            image = Image.open(question_image)
            while image.size[0]*c_w*const >= 175 or image.size[1]*c_w*const >= 150:
                c_w -= 0.05
                if c_w <= 0.05:
                    break
            image.close()
            width = image.size[0]*c_w*const
            quest_h = image.size[1]*c_w*const
        all_h = 9 + 72 + quest_h
        if better_answer[0]:
            all_h = all_h + 5
        if all_h+position > 282:
            self.add_page()

        self.question_title(num)
        self.question_body(question_image, chart, better_answer, width)

    def cover(self, examname, version):
        self.ln(110)
        self.set_font('Arial', 'B', 24)
        self.cell(190, 20, 'Results', 0, align='C')
        self.ln(20)
        self.set_font('Arial', 'B', 30)
        self.cell(190, 20, '{}  {}'.format(examname, version), 0, align='C')

    def total_stats(self, table, chart):
        self.set_y(30)
        self.set_font('Arial', 'B', 18)
        self.cell(190, 20, 'Total statistics', 0, align='C')
        self.ln(30)
        self.set_x(55)
        self.image(table, w=100)
        self.ln(20)
        self.image(chart, w=190)

#better answer will be list of lists
def create_report(examname, version, table_t, chart_t, charts, question_images, better_answers, destination):
    pdf = PDF()
    pdf.set_title(examname + ' ' + version)
    pdf.set_author('Results Analyzer')
    pdf.add_page()
    pdf.cover(examname, version)
    pdf.add_page()
    pdf.total_stats(table_t, chart_t)
    pdf.add_page()
    for q in range(1, len(charts)+1):
        if not question_images:
            pdf.print_question(q, False, charts[q-1], better_answers[q-1])
        else:
            pdf.print_question(q, question_images[q-1], charts[q-1], better_answers[q-1])
    pdf.output(os.path.join(destination, '{}_{}_results.pdf'.format(examname, version)), 'F')
