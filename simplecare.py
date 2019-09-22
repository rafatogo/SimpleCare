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
txt = open('Flex_Bronze.txt', 'r')
allLines = txt.readlines()
s = allLines[1]
s = s.strip(": ")
dataList["Plan Name"] = s[:-1]
deductibleFound = False
deductibleLocation = -1
outOfPocketLocation = -1
count = 0

def calcPremium(deductible):
    """
    calculates the premium relative to deductible
    """
    deductible = int((dataList["Deductible"].split()[0][1:]).replace(',', ''))
    if deductible < 700:
        dataList["Premium Level"] = "Higher Premium Level"
    elif deductible > 1400:
        dataList["Premium Level"] = "Lower Premium Level"
    else:
        dataList["Premium Level"] = "Medium Premium Level"
    
for line in allLines:
    if "Plan Type" in line:
        strList = line.split()
        planType = strList[-1]
        if planType == "HMO":
           dataList["Do I have to stay in network?"] = "Yes"
           dataList["Do I need a referal to see a specialist?"] = "Yes"
        elif planType == "PPO":
            dataList["Do I have to stay in network?"] = "No"
            dataList["Do I need a referal to see a specialist?"] = "No"
        elif planType == "EPO":
            dataList["Do I have to stay in network?"] = "Yes"
            dataList["Do I need a referal to see a specialist?"] = "No"
        elif planType == "POS":
            dataList["Do I have to stay in network?"] = "No"
            dataList["Do I need a referal to see a specialist?"] = "Yes"
        else:
            dataList["Do I have to stay in network?"] = "Yes"
            dataList["Do I need a referal to see a specialist?"] = "Yes"
        
    elif count==deductibleLocation:
        dataList["Deductible"] = line[:-1]
        
    elif count==outOfPocketLocation:
        dataList["OOP"] = line[:-1]
    
    elif (not deductibleFound) and "deductible?" in line:
        deductibleLocation = count+2
        deductibleFound = True
        
    elif "limit for this plan?" in line:
        outOfPocketLocation = count+2
        
    elif "% coinsurance" in line:
        coinsuranceIndex = line.index("% coinsurance")

    
    elif "Copayments" in line:
        copayLocation = line.index("Copayments")
        dataList["Copayment"] = line[copayLocation: +8]
    elif "NOT covered" in line:
        notCoveredList = []
        ncLocation = line.index("NOT Cover")
        endLocation = line.index("Other Covered Services")
        for l in allLines[ncLocation-1, endLocation]
            l.lstrip('• ')
            notCoveredList.append(l)
        dataList["NOT covered"] = notCoveredList
    else:
        pass
    count += 1
calcPremium (dataList["Deductible"])
    
"""
#close file


#1. plan name --> coinsurance
#2. plan type (planType) --> must stay in service yes/no, requires referel for specialist yes/no
#3. deductible
#4. out of pocket limit
#5. copay
#6. MA's algo --> premium
#7. NOT covered
