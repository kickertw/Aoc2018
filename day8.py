class Node:
    def __init__(self, kidCount = 0, metaData = [], isRoot = False):
        self.kids = []
        self.metaData = metaData
        self.isRoot = isRoot
        self.mdSum = 0

        if kidCount > 0:
            self.initKids(kidCount)
    
    def initKids(self, kidCount):
        for i in range(kidCount):
            self.kids.append(Node())

    def getMetaDataSum(self):
        if len(self.kids) == 0:
            return sum(self.metaData)

        subSum = 0
        for i in range(len(self.metaData)):
            childOfInterestIdx = self.metaData[i]-1
            if childOfInterestIdx < len(self.kids):
                subSum += self.kids[childOfInterestIdx].mdSum
        
        return subSum

def getIndentation(count):
    return "    " * count

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

def removeNodeFromInput(input, cursor, mdLen):
    input[:] = input[:cursor] + input[cursor+2+mdLen:]

def createTree(input, cursor, node, depth = 0):
    kidCount = input[cursor]
    mdLen = input[cursor+1]

    if cursor == 0:
        node = Node(kidCount, input[-mdLen:], True)
    else:
        node.initKids(kidCount)

    # if no kids, save the meta data and remove the node from the input
    if kidCount == 0:
        node.metaData = input[cursor+2:cursor+2+mdLen]
        node.mdSum = sum(node.metaData)
        removeNodeFromInput(input, cursor, mdLen)
        return node

    # recursively create child nodes
    for i in range(kidCount):
        node.kids[i] = createTree(input, cursor + 2, node.kids[i], depth+1)

    # after parsing all the kids, get the metadata so you know which ones to sum up
    node.metaData = node.metaData = input[cursor+2:cursor+2+mdLen]

    # while we're here, might as well get the metadata sum
    node.mdSum = node.getMetaDataSum()
    if not node.isRoot:
        removeNodeFromInput(input, cursor, mdLen)

    return node

mdSum = 0
p1Total = 0
ogInput = readInput()
inputList = ogInput.copy()

# Get the sum of the meta data of the root node and remove the root node
p1Total = sumMetaData(inputList, 0)
print("Part 1 total = {}".format(p1Total))

# Part 2
inputList = ogInput.copy()
rootMdLen = inputList[1]
rootNode = createTree(inputList, 0, None)
print("Part 2 total = {}".format(rootNode.mdSum))