import os

def countNames():
    file = open("namen.txt", "r")
    names = {}

    for line in file:
        if line not in names:
            names[line] = 0
        else: 
            names[line] += 1

    return names

def logResult(dictList):
    for result in dictList:
        print(f"{result} found : {dictList[result]}")

logResult(countNames())