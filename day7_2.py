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

def findRoot(steps, keys):
    for key in keys:
        if isRoot(steps, key):
            return key
    return None

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
p1Steps = steps
while len(currentRootNodes) > 0:
    p1Steps = processNodes(p1Steps, currentRootNodes, finalOrder)

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

def freeUpWorkers(workers, steps, finalOrder, currentTime):
    for worker in workers:
        if worker.active and currentTime == worker.isAvailableAt:
            steps = removeSteps(steps, worker.workingOn)
            worker.active = False
            worker.workingOn = None

    return steps

def hasActiveWorkers(workers):
    for worker in workers:
        if worker.active:
            return True
    return False

## Calculating the duration of each step per letter
alphabet = list(string.ascii_uppercase)
alphaWait = {}
for i, letter in enumerate(alphabet):
    alphaWait[letter] = 61 + i

currentTime = 0
worker1 = Worker(1)
worker2 = Worker(2)
workers = [worker1, worker2, Worker(3), Worker(4), Worker(5)]
while len(finalOrder) > 0 or hasActiveWorkers(workers):
    # Free up any workers that have just completed thier step
    if currentTime > 0:
        steps = freeUpWorkers(workers, steps, finalOrder, currentTime)

    # Find the first available worker.
    # If there is one, give them work and take that work off the list
    newWorker = findAvailableWorker(workers)
    nextRoot = findRoot(steps, finalOrder)
    while not (newWorker is None) and len(finalOrder) > 0 and not (nextRoot is None):
        newWorker.workingOn = nextRoot
        newWorker.active = True
        newWorker.isAvailableAt = currentTime + alphaWait[nextRoot]
        #print(" Worker {} is now assigned to {} and will be free at {} sec".format(newWorker.id, nextRoot, newWorker.isAvailableAt))
        finalOrder.remove(nextRoot)
        
        # Get the next available worker and the next root (if there are any)
        newWorker = findAvailableWorker(workers)
        nextRoot = findRoot(steps, finalOrder)

    currentTime += 1

print("All steps completed in {} seconds".format(currentTime - 1))