def findManhattenDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def grid_init(cols, rows):
    grid = [None] * rows
    for i in range(len(grid)):
        grid[i] = [None] * cols
    return grid

def isSafeCoordinate(currentPoint, coordinates):
    retVal = 0
    
    for point in coordinates:
        retVal += findManhattenDistance(currentPoint, point)
    
    return retVal < 10000

def calcSafeArea(grid):
    safeArea = sum(x.count(1) for x in grid)

    print("Largest Safe Area = {}".format(safeArea))

minX = 10000
maxX = 0
minY = 10000
maxY = 0
coordinates = []

with open("./inputs/day6.txt", "r") as f:
    for line in f:
        coord = line.split()
        x = int(coord[0][:-1])
        y = int(coord[1])

        minX = x if minX > x else minX
        maxX = x if maxX < x else maxX
        minY = y if minY > y else minY
        maxY = y if maxY < y else maxY
        coordinates.append((x, y))

grid = grid_init(maxX+1, maxY+1)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        currentPoint = (x, y)
        if isSafeCoordinate(currentPoint, coordinates):
            grid[y][x] = 1

calcSafeArea(grid)