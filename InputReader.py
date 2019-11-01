# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:42:11 2019

@author: NaVnEeT
"""
import pandas as pd
filename = input ("filename: ")
with open (filename, "w") as f:
    
Tankspecficationdata=input('Tank specfication data :')
Tanknumber=input('Tank number:')
Typeoftank=input('Type of tank:')
Itemname=input('Item name:')
Desingcode=input('Desing code:')
print('-------Input Design Parameters---------')
Nominalcapacity=input('Nominal capacity(cubicmeter):')
Insidediameter=input('Inside diameter(meter):')
tankheight=input('tank height(meter)')
maximumfillingheight=input('maximum filling height:') 
Htest=input('Htest:')
infillingrate=input('in-filling rate:')
Emptyingrate=input('Emptying rate:')
Productdensity20C=input('Product density @20C:')
Slopeatthebottom1=input('Slope at the bottom 1:')
print('------Enter Corrsion Allowance--------')
Shellcourse1=input('Shell (1st course):')
Shellcourse2=input('Shell (2nd course):')
bottom=input('Bottom:')
Ringofsketchplate=input('Ring of sketch plate:')
Roof=input('Roof:')
Designliquidheight=input('Design liquid height:')
Designspecificgravity=input('Design specific gravity:')
print('------Enter Internal Pressure------')
IPDesignconditionKpag=input('Design condition')
IPDesignconditionmmH2O=input('Design condition')
IPOperatingconditionKpag=input('Operating condition')
IPOperatingconditionmmH2O=input('Operating condition')
IPTestcondtionKpag=input('Test condition')
IPTestcondtionmmH2O=input('Test condition')
print('--------Enter External Pressure--------')
EPDesignconditionKpag=input('Design condition')
EPDesignconditionmmH2O=input('Design condition')
EPOperatingconditionKpag=input('Operating condition')
EPOperatingconditionmmH2O=input('Operating condition')
print('--------Enter Temperature--------')
TempDesigncondition=input('Design condition:')
TempOperatingconditionmin=input('Operating condition(min):')
TempOperatingconditionmax=input('Operating condition(max):')
Flashpoint=input('Flash point:')
print('---------------------')
Designwindspeed=input('Design wind speed (3 sec gust wind speed):')
Seismicdesign=input('Seismic design :')
Typeofroof=input('Al geodesic domre roof')
Frangibleroof=input('Frangible roof:')
HHLL=input('High-high liquid level :')
HLL=input('High liquid level:')
LLL=input('Low liquid level :')
LLLL=input('low Low liquid level :')
minThicknessbyclient=input('min. Thickness by client:')
minAnnularThicknessbyclient=input('min. Annular Thickness by client :')







