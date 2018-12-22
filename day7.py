import string

def removeSteps(steps, key):
    newSteps = []
    for i in range(len(steps)):
        if steps[i][0] != key:
            newSteps.append(steps[i])
    return newSteps

def isRoot(steps, key):
    for tpl in steps:
        if tpl[1] == key:
            return False
    return True

# 1 - Add the root node to the final order
# 2a - Remove it from the current root list
# 2b - Remove it from the steps list
# 3 - Add children (that have no parent) to the current root list
# 4 - sort the current root list
def processNodes(steps, currentRootNodes, finalOrder):
    currentRoot = currentRootNodes[0]

    finalOrder.append(currentRoot)
    currentRootNodes.remove(currentRoot)
    childrenOfRoot = [item[1] for item in steps if item[0] == currentRoot]
    steps = removeSteps(steps, currentRoot)
    for kid in childrenOfRoot:
        if isRoot(steps, kid):
            currentRootNodes.append(kid)
    
    currentRootNodes.sort()
    return steps



steps = []
finalOrder = []
keys = list(string.ascii_uppercase)

with open("./inputs/day7.txt", "r") as f:
    for line in f:
        nodeA = line[5:6]
        nodeB = line[36:37]
        step = (nodeA, nodeB)
        steps.append(step)
        if nodeB in keys:
            keys.remove(nodeB)

currentRootNodes = keys
currentRootNodes.sort()
while len(currentRootNodes) > 0:
    steps = processNodes(steps, currentRootNodes, finalOrder)

print(''.join(finalOrder))