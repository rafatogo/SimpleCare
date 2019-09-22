#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:03:57 2019
@author: marie-annexu
"""
"""
#convert pdf to text file
#import text file
#need plan name, type, and deductible
#open(text file, rt)
#for line in text file:
    #if search phrase in textfile:
        #print line(s) 
"""
easyCompareList = list()

while True:
    fileName = input('File Name: ')
    if fileName != 'done':
        dataList = {}
        txt = open(fileName, encoding = "utf8")
        allLines = txt.readlines()
        s = allLines[1]
        s = s.strip(": ")
        dataList["Plan Name"] = s[:-1]
        deductibleFound = False
        deductibleLocation = -1
        outOfPocketLocation = -1
        copayLocation = -1
        count = 0
        notCoveredLine = 0
        coveredLine = 0
        def calcPremium(deductible):

        #calculates the premium relative to deductible

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
                    dataList["Do I need a referral to see a specialist?"] = "Yes"
                elif planType == "PPO":
                    dataList["Do I have to stay in network?"] = "No"
                    dataList["Do I need a referral to see a specialist?"] = "No"
                elif planType == "EPO":
                    dataList["Do I have to stay in network?"] = "Yes"
                    dataList["Do I need a referral to see a specialist?"] = "No"
                elif planType == "POS":
                    dataList["Do I have to stay in network?"] = "No"
                    dataList["Do I need a referral to see a specialist?"] = "Yes"
                else:
                    dataList["Do I have to stay in network?"] = "Yes"
                    dataList["Do I need a referral to see a specialist?"] = "Yes"

            elif count==deductibleLocation:
                dataList["Deductible"] = line[:-1]

            elif count==outOfPocketLocation:
                dataList["OOP"] = line[:-1]

            elif count == copayLocation:
                dataList["Copayment"] = line.split()[0]
                if '$' not in dataList["Copayment"]:
                    dataList["Copayment"] = "$0"

            elif (not deductibleFound) and "deductible?" in line:
                deductibleLocation = count+2
                deductibleFound = True

            elif "limit for this plan?" in line:
                outOfPocketLocation = count+2

            elif "% coinsurance" in line:
                coinsuranceIndex = line.index("% coinsurance")
            elif "injury or illness" in line:
                copayLocation = count + 2

            elif "NOT Cover" in line:
                notCoveredLine = count + 1

            elif "Other Covered Services" in line:
                coveredLine = count

            else:
                pass

            count += 1

        notCoveredList = []
        lines = allLines[notCoveredLine:coveredLine]
        for line in lines:
            notCoveredList.append(line[2:-1])
        dataList["NOT covered"] = notCoveredList

        calcPremium (dataList["Deductible"])

        print(dataList)
        easyCompareList.append(dataList)

        txt.close()
    else:
        break

def getTable(dataLists):
    table = []
    keyList = []
    for key in dataLists[0].keys():
        keyList.append(key)
        for dataList in dataLists:
            keyList.append(dataList[key])
        table.append(keyList)
        keyList = []
    return table

def printTable(table):
    for l in table:
        print(l)

printTable(getTable(easyCompareList))


#close file


#1. plan name --> coinsurance
#2. plan type (planType) --> must stay in service yes/no, requires referel for specialist yes/no
#3. deductible
#4. out of pocket limit
#5. copay
#6. MA's algo --> premium
#7. NOT covered
