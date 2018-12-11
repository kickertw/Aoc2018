import re
import string

def getReducedPolymerLen(inputString):
    outputString = ""
    while len(inputString) > 0:
        if len(outputString) > 0 and outputString[-1].swapcase() == inputString[0]:
            outputString = outputString[:-1]
        else:
            outputString += inputString[0]
        inputString = inputString[1:]
    return len(outputString)

with open("./inputs/day5.txt", "r") as f:
    cursor = 0
    ogInputString = f.read().splitlines()[0]

shortestPolyLen = len(ogInputString)
for key in string.ascii_lowercase:   
    reKey = "[{}{}]".format(key, key.upper())
    inputString = re.sub(reKey, '', ogInputString)
    rpLen = getReducedPolymerLen(inputString)
    if rpLen < shortestPolyLen:
        shortestPolyLen = rpLen

print(shortestPolyLen)