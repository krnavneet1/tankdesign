# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:40:33 2019

@author: NaVnEeT
"""
import math
import PDFconverter
def InternalPressure(Internalpress):
    if Internalpress<1:
        internalpressure=0
    else:
        internalpressure=1
    return(internalpressure)
def CourseHeight(tankheight,shellcount):
    crshgt=tankheight/shellcount
    return(crshgt)
def PrelimDesignCond(D,H,G,P,CA,Sd,IP):
    print(D,H,G,P,CA,Sd,IP)
    tpd=((4.9*D*(((H-0.3)*G)+((P/9.8)*IP)))/Sd)+CA
    return(tpd)

def PrelimHydrostaticCond(D,Htest,Pt,St,IP):
    tpt=(4.9*D*(((Htest-0.3))+((Pt/9.8)*IP)))/St
    return(tpt)

def BottomCourseDesignCond(D,H,G,P,CA,Sd):
    var1=math.sqrt(((H+(P/(9.8*G)))*G)/Sd)
    var2=(0.0696*D)/(H+(P/(9.8*G)))
    var3=(4.9*D*G*(H+(P/(9.8*G))))/Sd
    t1d=(1.06-(var1*var2))*var3+CA
    return(t1d)

def BottomHydrostaticCond(D,Htest,Pt,St):
    var1=math.sqrt((Htest+(Pt/9.8))/St)
    var2=(0.0696*D)/(Htest+(Pt/9.8))
    var3=(4.9*D*(Htest+(Pt/9.8)))/St
    t1t=(1.06-(var1*var2))*var3
    return(t1t)

def SecondCourseThickness(h,r,t,t1,t2a):
    var=h/(math.sqrt(r*t))
    if var<=1.375:
        t2=t1
    if var>=2.625:
        t2=t2a
    if var>1.375 and var<2.625:
        t2=t2a+((t1-t2a)(2.1-(h/(1.25*(math.sqrt(r*t))))))
    return(t2)

def UpperShellThicknessDesignCond(D,H,X,G,Sd,CA):
    tdx=((4.9*D*(H-(X/1000))*G)/Sd)+CA
    return(tdx)

def UpperShellThicknessHydrostaticCond(D,Htest,X,St):
    ttx=(4.9*D*(Htest-(X/1000)))/St
    return(ttx)
    
    



def shellinput(Designspecificgravity,IPDesignconditionKpag,IPTestcondtionKpag,DOCNo,Tanknumber,Typeoftank,Itemname,Designcode,
               shells,shellCA,Insidediameter,tankheight,maximumfillingheight,Htest,HHLL,HLL,LLL,LLLL,Nominalcapacity,InputPath):
    if shells =='A573 Gr.70 ':
        print('T')
        Ft=485
        Fy=290
        Sd=193
        St=208
    else:
        Ft=380
        Fy=205
        Sd=137
        St=154
    tpd=PrelimDesignCond(Insidediameter,maximumfillingheight,Designspecificgravity,IPDesignconditionKpag,shellCA,Sd,InternalPressure(IPDesignconditionKpag))
    tpt=PrelimHydrostaticCond(Insidediameter,Htest,IPTestcondtionKpag,St,InternalPressure(IPTestcondtionKpag))
    Courseheight=CourseHeight(tankheight,len(shells))
    tmin=max(tpd,tpt)
    tabl=[[Courseheight,shells,Sd,tpd,St,tpt,tmin,round(tmin)],[]]
    PDFconverter.createpdf(DOCNo,Tanknumber,Typeoftank,Itemname,Designcode,Nominalcapacity,InputPath,tabl)
        
            
    
    
