def countNames():
    with open("namen.txt", "r", encoding="utf-8") as file:
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