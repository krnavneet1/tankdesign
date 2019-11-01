# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:43:01 2019

@author: kanupam
"""

import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
df = pd.DataFrame()
from IPython.display import Image
from sympy import pretty_print as pp, latex
from sympy.abc import a, b, n

def createpdf(Docno, Tankno, Typeoftank,Itemname, Designcode, NOMINALCAPACITY,InputPath,tabl):
#General variables
    smallfontsize=10
    midfontsize=12
    largefontsize=16
    thickness=[["Course","Course","Material","Design Thickness","","Hydrotests","thickness","",""],["","Height","","  Sd","  td","  St","  tt","  tmin","  tused"],] 
    pdf = FPDF()
    pdf.add_page()
    
    #page 1 define variables
    spacing=20
    startingspacing=50
    margin=55
    #page 1 document number
    pdf.set_font('Arial', 'B', smallfontsize)
    pdf.set_xy(150,14)
    pdf.cell(5,5, 'Document no. ' +Docno,'C') 
    pdf.set_xy(50,14)
    pdf.set_font('Arial', 'B', largefontsize )
    pdf.cell(5,5,'TANK DESIGN CALCULATION','C') 
    # Description
    
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '1. TANK DESIGN DATA','C') 
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '2. TANK CAPACITY','C') 
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '3. SHELL DESIGN ','C')
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '4. BOTTOM PLATE ','C') 
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '5. COMPRESSION RING AREA DESIGN (HOLD) ','C') 
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '6. PRIMARY WIND GRIDER DESIGN ','C') 
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '7. STABILITY OF SHELL AGAINST WIND ','C') 
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '8. TENSION RING AREA DESIGN (HOLD) ','C')
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '9. OVERTURNING STABILITY CHECK (HOLD) ','C')
    startingspacing=startingspacing+spacing
    pdf.set_xy(margin,startingspacing)
    pdf.set_font('Arial', 'B', midfontsize)
    pdf.cell(5,5, '10. TANK COMPONENTS WEIGHT CALCULATION (HOLD) ','C')
    
    
    
    #
    #page 2 define variables
    marginfirstchar=25
    marginfirstcharshift=15
    marginsecondchar=marginfirstchar+50
    marginsecondcharshift=0
    marginthirdchar=marginfirstchar+marginfirstcharshift
    marginfourthchar=marginthirdchar+4*marginfirstcharshift
    marginfifthchar=marginfourthchar+2*marginfirstcharshift
    
    topmargin=20
    topmarginspacing=5
    
    #
    pdf.add_page()
    #
    topmargin=topmargin+2*topmarginspacing
    pdf.set_xy(marginfirstchar,topmargin)
    pdf.set_font('Arial', 'B', midfontsize )
    pdf.cell(5,5, '1.   TANK DESIGN DATA                   ','C') 
    pdf.set_xy(marginsecondchar,topmargin)
    #
    topmargin=topmargin+2*topmarginspacing
    pdf.set_xy(marginfirstchar,topmargin)
    pdf.set_font('Arial', 'B', smallfontsize )
    pdf.cell(5,5, '1.1  TANK NO.                   ','C') 
    pdf.set_xy(marginsecondchar,topmargin)
    pdf.set_font('Arial', 'U', smallfontsize )
    pdf.cell(5,5,Tankno,'C') 
    #
    topmargin=topmargin+topmarginspacing
    pdf.set_xy(marginfirstchar,topmargin)
    pdf.set_font('Arial', 'B', smallfontsize )
    pdf.cell(5,5, '1.2  TYPE OF TANK                   ','C') 
    pdf.set_xy(marginsecondchar,topmargin)
    pdf.set_font('Arial', 'U', smallfontsize )
    pdf.cell(5,5,Typeoftank,'C') 
    #
    topmargin=topmargin+topmarginspacing
    pdf.set_xy(marginfirstchar,topmargin)
    pdf.set_font('Arial', 'B', smallfontsize )
    pdf.cell(5,5, '1.3  ITEM NAME                   ','C') 
    pdf.set_xy(marginsecondchar,topmargin)
    pdf.set_font('Arial', 'U', smallfontsize )
    pdf.cell(5,5,Itemname,'C') 
    #
    topmargin=topmargin+topmarginspacing
    pdf.set_xy(marginfirstchar,topmargin)
    pdf.set_font('Arial', 'B', smallfontsize )
    pdf.cell(5,5, '1.4  DESIGN CODE                   ','C') 
    pdf.set_xy(marginsecondchar,topmargin)
    pdf.set_font('Arial', 'U', smallfontsize )
    pdf.cell(5,5,Designcode,'C') 
    #
    topmargin=topmargin+2*topmarginspacing
    pdf.set_xy(marginfirstchar,topmargin)
    pdf.set_font('Arial', 'B', smallfontsize )
    pdf.cell(5,5, '1.5  DESIGN DATA                   ','C') 
    pdf.set_xy(marginsecondchar,topmargin)
    #
    topmargin=topmargin+2*topmarginspacing
    pdf.set_xy(marginthirdchar,topmargin)
    pdf.set_font('Arial', 'B', smallfontsize )
    pdf.cell(5,5, '1.5.1  NOMINAL CAPACITY                   ','C') 
    pdf.set_xy(marginfourthchar,topmargin)
    pdf.set_font('Arial', 'U', smallfontsize )
    pdf.cell(5,5,str(NOMINALCAPACITY),'C') 
    pdf.set_xy(marginfifthchar,topmargin)
    pdf.set_font('Arial', '', smallfontsize )
    pdf.cell(5,5,f'm\N{SUPERSCRIPT THREE}' ,'C') 
    
    #
    topmargin=topmargin+2*topmarginspacing
    pdf.set_xy(marginthirdchar+50,topmargin+50)
    pdf.set_font('Arial', 'B', 20 )
    pdf.cell(5,5, 'Demo:Rest to be developed    ','C') 
    #        
    pdf.add_page()
        #variables
    topmargin=20
    marginfirstchar=25
    width=20
    row=5
    #noofrows=2
    #noofcol=8
    
    pdf.set_font('Arial', 'B', smallfontsize )
    #set cursor
    for tempcol in thickness:
        marginfirstchar=25
        for temprow in tempcol:
               pdf.set_xy(marginfirstchar,topmargin)
               marginfirstchar=marginfirstchar+width
               pdf.cell(5,5, temprow,'C') 
        topmargin=topmargin+row
    for newtempcol in tabl:
        marginfirstchar=25
        for newtemprow in newtempcol:
               pdf.set_xy(marginfirstchar,topmargin)
               marginfirstchar=marginfirstchar+width
               pdf.cell(5,5, str(newtemprow),'C') 
        topmargin=topmargin+row
   
    
    #page 2 define variables
#    marginfirstchar=25
#    marginfirstcharshift=15
#    topmargin=20
#    topmarginspacing=5
#    col_width = 20
#    row_height = 10
#    spacing=1
#    #
#    pdf.add_page()
#    #Calculation
#    topmargin=topmargin+topmarginspacing
#    pdf.set_xy(marginfirstchar,topmargin)
#    pdf.set_font('Arial', 'B', midfontsize )
#    pdf.cell(5,5, '3.3  CALCULATION AND RESULT                   ','C') 
#    pdf.set_xy(marginsecondchar,topmargin)
#    #
#    topmargin=topmargin+topmarginspacing
#    #pdf.set_xy(marginsecondchar,topmargin)
#    pdf.set_font('Arial', '', smallfontsize )
    #create data
    
    #SAVE-----------------------
    pdf.output(InputPath+'\\tankdesign1.pdf', 'F')  
    
#tabl=[[3.5, 5.6,.666,6.5,8.555,9.555,2.55],['C','CH','M','DT','HT','tmin','tused']]
#createpdf('D', 'Tankno', 'Typeoftank','Itemname', 'Designcode', 'NOMINALCAPACITY','D:\\tankdesign',tabl)