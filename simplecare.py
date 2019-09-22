#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:03:57 2019

@author: marie-annexu
"""

#convert pdf to text file
#import text file
#need plan name, type, and deductible
#open(text file, rt)
#for line in text file:
    #if search phrase in textfile:
        #print line(s) 
"""
dataList = {}
txt = imported text file
allLines = txt.readLine()
s = allLines[2]
s.strip(": ")
dataList["Plan Name"] = s
with open('imported text file', 'r') as f:
    for line in txt:
        if "Plan Type: " in line:
            string = str(line)
            strList = string.split()
            dataList["Plan Type"] = strList(len(strList)-1)
        else:
            pass
with open('imported text file', 'r') as f:
    data = f.readlines()
line_no = data.index("Plan Type:")
while text file != "":
    if "deductible?" in text file:
        deductibleLocation = line.index("deductible?")

        dataList["deductible"] = line[deductibleLocation: +1]

    else:
        pass

"""
#close file


#1. plan name --> coinsurance
#2. plan type (planType) --> must stay in service yes/no, requires referel for specialist yes/no
#3. deductible
#4. out of pocket limit
#5. copay
#6. MA's algo --> premium
