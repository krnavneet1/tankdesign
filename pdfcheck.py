# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:08:53 2019

@author: kanupam
"""

import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
df = pd.DataFrame()
from IPython.display import Image
#Image("download.jpg")

#pdf.cell(75, 10, "A Tabular and Graphical Report of Professor Criss's Ratings by Users Charles and Mike", 0, 2, 'C')

#savefig('barchart.png')
a=3
b=5
c=a+b
print(c) 
pdf = FPDF()
pdf.add_page()
#pdf.cell(75, 10, "A Tabular and Graphical Report of Professor Criss's Ratings by Users Charles and Mike", 0, 2, 'C')
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!',0,1)
pdf.image('download.jpg', x = None, y = None, w = 0, h = 0, type = '', link = '')
pdf.cell(100, 100,str(c),0,1)
pdf.output('test.pdf', 'F')