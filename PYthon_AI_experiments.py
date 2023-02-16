from ast import Constant
from base64 import b16decode
from msilib.schema import AdminExecuteSequence
from operator import ge, truediv
from tkinter import *
import random
import cmath
import math
from tkinter.tix import WINDOW

import uuid




def SpawningDots(input1):
 #input 1 = dotammount
 cout=0
 global reddots
 global bluedots
 reddots=[]
 bluedots=[]
 if (input1 % 2) == 0:
   hlf = int(input1 / 2)
   hlf2 = int(input1 / 2)
 else:
   hlf = int((input1+1)/2)
   hlf2 = int((input1-1) / 2)
  
   #creating red dots, i think

 for i in range(hlf):
  rx = random.randint(1, GAME_WIDTH)
  ry = random.randint(1, GAME_HEIGHT)

  ovlred =canvas.create_oval(rx-14, ry-14, rx+14, ry+14, outline="#456789",
            fill="#F9093C", width=3, tags= "ovldel")

  
  cout= cout+1
  reddots.append(rx)
  reddots.append(ry)

  #creating blue dots
 for i in range(hlf2):
  rx = random.randint(1, GAME_WIDTH)
  ry = random.randint(1, GAME_HEIGHT)

  ovlblue=canvas.create_oval(rx-14, ry-14, rx+14, ry+14, outline="#456789",
            fill="#095DF9", width=3,tags= "ovldel")
  cout= cout+1
  bluedots.append(rx)
  bluedots.append(ry)




  




def creatingwindow():
    
 global GAME_WIDTH
 global GAME_HEIGHT 
 global SPEED 
 global SPACE_SIZE 
 global BODY_PARTS 

 
 
 
 GAME_WIDTH= 986
 GAME_HEIGHT = 700
 SPEED = 50
 SPACE_SIZE = 50
 BODY_PARTS = 3

 BACKGROUND_COLOR = "#000000"



 global window
 window= Tk()
 window.title("Spreading Dots")
 window.resizable(False, False)

 global canvas 
 canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
 canvas.pack()

 global label
 label = Label(window, text="".format(1), font=('consolas', 40))
 label.pack()


 


 
def ResettingDots():
 reddots.clear()
 bluedots.clear()
 canvas.delete("ovldel")
 SpawningDots(dotammount)




 


def Calcing_line_Coords( existing_bias, biast_x1,biast_y1, biast_x2, biast_y2  ):
    #this function calculates the location of the 2 endpoints of a line
    #existing_bias asks (in bool) weather we already have a bias for a  new line
    #the biast variables stand for those biast coordinates. (if none exist, replace with 0 or leave empty)
    x1=0
    y1=0
    x2=0
    y2=0
    if (existing_bias== TRUE):
  

     #stupid shite
     if(biast_x1== GAME_WIDTH or biast_x1 == 0):
         x1= biast_x1
     else:
         newvalue = random.randint(biast_x1-50, biast_x1+50)
         if (newvalue == GAME_WIDTH or newvalue == 0):
             x1= biast_x1
         else: 
             x1= newvalue

     if(biast_y1== GAME_HEIGHT or biast_y1 == 0):
         y1= biast_x1
     else:
         newvalue = random.randint(biast_y1-50, biast_y1+50)
         if (newvalue == GAME_HEIGHT or newvalue == 0):
             y1= biast_y1
         else: 
             y1= newvalue



     if(biast_x2== GAME_WIDTH or biast_x2 == 0):
         x2= biast_x2
     else:
         newvalue = random.randint(biast_x2-50, biast_x2+50)
         if (newvalue == GAME_WIDTH or newvalue == 0):
             x2= biast_x2
         else: 
             x2= newvalue

     if(biast_y2== GAME_HEIGHT or biast_y2 == 0):
         y2= biast_x2
     else:
         newvalue = random.randint(biast_y2-50, biast_y2+50)
         if (newvalue == GAME_HEIGHT or newvalue == 0):
             y2= biast_y2
         else: 
             y2= newvalue



    else:

     #1 is top, 2 is right, 3 is bottom, 4 is left
     rndm =random.randint(1,4)
     #1st dot:
     if(rndm==1):
         y1=GAME_HEIGHT
         x1= random.randint(1, GAME_WIDTH-1)
     if(rndm==2):
         x1=GAME_WIDTH
         y1=random.randint(1, GAME_HEIGHT-1)
     if(rndm==3):
         y1=0
         x1= random.randint(1, GAME_WIDTH-1)
     if(rndm ==4):
         x1=0
         y1=random.randint(1, GAME_HEIGHT-1)
     #2nd dot:
     #checking that dot1 and dot2 are not on the same side (cuz that would frick things up)
     rndm2 =random.randint(1,4)
     same=TRUE
     while same:
         if (rndm2 == rndm):
          rndm2 =random.randint(1,4)
         else:
          same=FALSE
      
          
     if(rndm2==1):
         y2=GAME_HEIGHT
         x2= random.randint(1, GAME_WIDTH-1)
     if(rndm2==2):
         x2=GAME_WIDTH
         y2=random.randint(1, GAME_HEIGHT-1)
     if(rndm2==3):
         y2=0
         x2= random.randint(1, GAME_WIDTH-1)
     if(rndm2 ==4):
         x2=0
         y2=random.randint(1, GAME_HEIGHT-1)
    xyz= [x1, y1, x2, y2]

     
    return xyz
        









  
def SeperatingDotsToSides(BothVariables_of_line):
  
    #calculating the basic vector 

 
    BluedotsInBlue=[]
    BluedotsInRed=[]
    ReddotsInBlue=[]
    ReddotsInRed=[]

    #positive angle = Blue Area
  
    bldts= len(bluedots)
    rddots=len(reddots)
    #starting with blue dots
    i=0
    while i <bldts:
   
     x1 = BothVariables_of_line[0]
     y1 = BothVariables_of_line[1]
     x2 = BothVariables_of_line[2]
     y2 = BothVariables_of_line[3]
     x3 = bluedots[i]
     y3= bluedots[i+1]

     angle = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)



     if(angle >=0):
         BluedotsInBlue.append(bluedots[i])
         BluedotsInBlue.append(bluedots[i+1])
     else:
       BluedotsInRed.append(bluedots[i])
       BluedotsInRed.append(bluedots[i+1])
  
   
    
     i=i+2
   


    
       
    i=0
    while i <rddots:


     x1 = BothVariables_of_line[0]
     y1 = BothVariables_of_line[1]
     x2 = BothVariables_of_line[2]
     y2 = BothVariables_of_line[3]
     x3 = reddots[i]
     y3= reddots[i+1]

     angle = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

     if(angle >=0):
         ReddotsInBlue.append(reddots[i])
         ReddotsInBlue.append(reddots[i+1])
     else:
       ReddotsInRed.append(reddots[i])
       ReddotsInRed.append(reddots[i+1])
     
   

     i=i+2
     
    
    return BluedotsInBlue, BluedotsInRed, ReddotsInBlue, ReddotsInRed
   
     

def Calculating_goodDistance(coordz, bbcoords, brcoords, rbcoords, rrcoords):
 goodDistance=[]
 badDistance=[]
 b= [coordz[2]-coordz[0], coordz[3]-coordz[1]]
 bb= math.sqrt(b[0]*b[0] + b[1]*b[1])

 bbclen=len(bbcoords)
 brclen=len(brcoords)
 rbclen=len(rbcoords)
 rrclen=len(rrcoords)

 

 i=0
 while i<bbclen:
  dotcoordz= bbcoords
  a=[dotcoordz[i]-coordz[0],dotcoordz[i+1]-coordz[1]]
  F= (a[0]*b[1]-a[1]*b[0])
  F=F / bb
  F= F*F
  F= math.sqrt(F)
  goodDistance.append(F)
  i=i+2
 i=0
 while i<brclen:
  dotcoordz= brcoords
  a=[dotcoordz[i]-coordz[0],dotcoordz[i+1]-coordz[1]]
  F= (a[0]*b[1]-a[1]*b[0])
  F=F/bb
  F= F*F
  F= math.sqrt(F)
  badDistance.append(F)
  i=i+2
 i=0
 while i<rbclen:
  dotcoordz= rbcoords
  a=[dotcoordz[i]-coordz[0],dotcoordz[i+1]-coordz[1]]
  F= (a[0]*b[1]-a[1]*b[0])
  F=F/bb
  F= F*F
  F= math.sqrt(F)
  badDistance.append(F)
  i=i+2
 i=0
 while i<rrclen:
  dotcoordz= rrcoords
  a=[dotcoordz[i]-coordz[0],dotcoordz[i+1]-coordz[1]]
  F= (a[0]*b[1]-a[1]*b[0])
  F=F/bb
  F= F*F
  F= math.sqrt(F)
  goodDistance.append(F)
  i=i+2

 return goodDistance, badDistance



def evaluating_distance(gooddist, baddist, coordz,recordValue,recordCoordz):
    
    savedist=0
   
    i=0
    ln=len(baddist)
    while i<ln:
        result= baddist[i]
        result = -1*(math.exp(-5*result))+1
        if(result>0.9999 ):
            result=1
        savedist= savedist+result
        i=i+1

    if(savedist <recordValue):
        return coordz, savedist

    savedist=0
    i=0
    ln=len(gooddist)
    while i<ln:
        result= gooddist[i]
        result = -1*(math.exp(-5*result))+1
        if(result>0.9999 ):
            result=1
        savedist= savedist+result
        i=i+1

    if(savedist <recordValue):
        return coordz, savedist

    else:
        return recordCoordz, recordValue


def Stupidcalculationshit(calculationdepth):
  #needs some fixing
    calcammount= [300,750,1500,6000,20,50,50,50]

  
    if (calculationdepth != 1 and calculationdepth != 2 and calculationdepth != 3 and calculationdepth != 4):
        calculationdepth= 4
 
 


    recordValue = 99999999.9
    recordCoordz=[]


    i=0
    while i<calcammount[calculationdepth-1]:

     coordz=Calcing_line_Coords(FALSE, 0,0,0,0)
     bbcoords, brcoords, rbcoords, rrcoords = SeperatingDotsToSides(coordz)
     goodist, baddist =Calculating_goodDistance(coordz, bbcoords, brcoords, rbcoords, rrcoords)
     recordCoordz, recordValue=evaluating_distance(goodist, baddist, coordz,recordValue,recordCoordz)
     i=i+1
     
    


    
    i=0
    while i<calcammount[calculationdepth+3]:

     coordz=Calcing_line_Coords(TRUE, recordCoordz[0],recordCoordz[1],recordCoordz[2],recordCoordz[3])
     bbcoords, brcoords, rbcoords, rrcoords = SeperatingDotsToSides(coordz)
     goodist, baddist =Calculating_goodDistance(coordz, bbcoords, brcoords, rbcoords, rrcoords)
     recordCoordz, recordValue=evaluating_distance(goodist, baddist, coordz,recordValue,recordCoordz)
     i=i+1
     
    infline = canvas.create_line(recordCoordz[0], recordCoordz[1], recordCoordz[2],recordCoordz[3], fill= "white",tags= "ovldel")



global dotammount

print("")
print("")
print("SETTINGS ")
print("")
print("")
print("How many dots do you want?")


dotammount = int(input())
print("")
print("CALCULATION DEPTH:  ")
print("1= low")
print("2= medium")
print("3= high")
print("4= might crash your computer")
calculationdepth = int(input())

creatingwindow()
SpawningDots(dotammount)






button = Button(window, text='Reset', width=30, command=ResettingDots)
button.pack()


button = Button(window, text='Calculate Middle', width=30, command=lambda:Stupidcalculationshit(calculationdepth))
button.pack()












window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()




window.mainloop()




