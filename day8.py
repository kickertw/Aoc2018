
def readInput():
    with open("./inputs/day8.txt", "r") as f:
        input = list(map(int, f.readline().split()))
    return input

def sumMetaData(input, cursor):
    mdLen = input[cursor+1]
    total = 0

    while input[cursor] > 0:
        subTot = sumMetaData(input, cursor + 2)
        total += subTot
        input[cursor] -= 1

    # 1. Get the metadata sum / 2. remove the node from the input
    total += sum(input[cursor+2:cursor+2+mdLen])
    input[:] = input[:cursor] + input[cursor+2+mdLen:]
    return total

mdSum = 0
p1Total = 0
input = readInput()

# Get the sum of the meta data of the root node and remove the root node
p1Total = sumMetaData(input, 0)

print("Part 1 total = {}".format(p1Total))