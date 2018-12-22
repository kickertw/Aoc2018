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
keys = ['A','B','C','D','E','F'] #list(string.ascii_uppercase)

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

print("Part 1 Order = " + ''.join(finalOrder))

## PART 2
class Worker:
    def __init__(self, id):
        self.id = id
        self.active = False
        self.workingOn = None
        self.isAvailableAt = 0

def findAvailableWorker(workers):
    for worker in workers:
        if not worker.active:
            return worker
    return None

def freeUpWorkers(workers, currentTime):
    for worker in workers:
        if worker.active and currentTime == worker.isAvailableAt:
            worker.active = False

def hasActiveWorkers(workers):
    for worker in workers:
        if worker.active:
            return True
    return False

alphabet = list(string.ascii_uppercase)
alphaWait = {}
for i, letter in enumerate(alphabet):
    alphaWait[letter] = 1 + i

currentTime = 0
worker1 = Worker(1)
worker2 = Worker(2)
workers = [worker1, worker2]#, Worker(3), Worker(4), Worker(5)]
while len(finalOrder) > 0 or hasActiveWorkers(workers):
    print(currentTime)
    # Free up any workers that have just completed thier step
    freeUpWorkers(workers, currentTime)

    # Find the first available worker.
    # If there is one, give them work and take that work off the list
    newWorker = findAvailableWorker(workers)
    if not (newWorker is None) and len(finalOrder) > 0:
        newWorker.workingOn = finalOrder[0]
        newWorker.active = True
        newWorker.isAvailableAt = currentTime + alphaWait[finalOrder[0]]
        print("Worker {} is now assigned to {} and will be free at {} sec".format(newWorker.id, finalOrder[0], newWorker.isAvailableAt))

        if len(finalOrder) > 1:
            finalOrder = finalOrder[1:]
        else:
            finalOrder = ""

    currentTime += 1

print(currentTime)