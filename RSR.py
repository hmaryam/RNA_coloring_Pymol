# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 11:11:23 2014

@author: Poorna
"""
import cmd
import csv

rsr=[]
f = open("rRNA Helices.csv", "rb")
for color,row in enumerate(csv.reader(f)):
        rsr.append([row[0],float(row[1])])

f.close()




for i in range(0,length(ColorCode)):
  if NucleotideRange(i) & ColorCode(i):
    if NucleotideRange(i) has “/” in it:
      FirstRange, SecondRange = SplitTwoRanges(NucleotideRange(i))
      a,b = SplitOneRange(FirstRange)
      OutputLine = MakeID(PDBID,"1",Chain(i),a) + "," + MakeID(PDBID,"1",Chain(i),b)) +"," + ColorCode(i)
      OutputText.append(OutputLine)
      a,b = SplitOneRange(SecondRange)
      OutputLine = MakeID(PDBID,"1",Chain(i),a) + "," + MakeID(PDBID,"1",Chain(i),b)) +"," + ColorCode(i)
      OutputText.append(OutputLine)
    



bg_color (color = "white")
        
for index,row in rsr:
     j=i.split("_")

cmd.bg_color (color = "white")
        

cmd.color("purpleblue", "4QS1 and resi "+'8')

cmd.color("purpleblue", "4QS1 and resi "+ j[5])

cmd.color("purpleblue", "4QS1 and resi "+ j[6])

cmd.color("purpleblue", "4QS1 and resi "+ j[7])    

### cut below here and paste into script ###
cmd.set_view ("""
    -0.651273787,    0.669810474,    0.356645435,\
     0.400719136,    0.702678859,   -0.587933362,\
    -0.644411325,   -0.239990935,   -0.726043105,\
     0.000000000,    0.000000000, -737.353515625,\
    90.952728271,    1.948154449,  -12.275173187,\
   611.372558594,  863.334594727,  -20.000000000""" )
### cut above here and paste into script ###


