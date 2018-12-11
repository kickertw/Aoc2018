with open("./inputs/day5.txt", "r") as f:
    cursor = 0
    inputString = f.read().splitlines()[0]
    outputString = ""

    while len(inputString) > 0:
        if len(outputString) > 0 and outputString[-1].swapcase() == inputString[0]:
            outputString = outputString[:-1]
        else:
            outputString += inputString[0]
        inputString = inputString[1:]

print(len(outputString))