def findManhattenDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def findClosestCoordinate(currentPoint, coordinates):
    distList = [0] * len(coordinates)
    for i, coord in enumerate(coordinates):
        dist = findManhattenDistance(currentPoint, coord)
        distList[i] = (i, dist)
    distList = sorted(distList, key=lambda x: x[1])

    if distList[0][1] == distList[1][1]:
        return -1

    return distList[0][0]

def grid_init(cols, rows):
    grid = [None] * rows
    for i in range(len(grid)):
        grid[i] = [None] * cols
    return grid

def findLargestFiniteArea(minX, maxX, minY, maxY, coordinates, grid):
    largestArea = 0
    searchableCoords = list(range(len(coordinates)))
    
    #removing an infinite coordinate if they hit the top edge
    for idx in grid[0]:
        if idx in searchableCoords:
            searchableCoords.remove(idx)
    
    #removing an infinite coordinate if they hit the bottom edge
    for idx in grid[maxY]:
        if idx in searchableCoords:
            searchableCoords.remove(idx)

    #removing an infinite coordinate if they hit the side edges
    for row in range(1, maxY):
        if grid[row][0] in searchableCoords:
            searchableCoords.remove(grid[row][0])
        if grid[row][maxX] in searchableCoords:
            searchableCoords.remove(grid[row][maxX])

    for i in searchableCoords:
        currentSum = sum(x.count(i) for x in grid)
        if currentSum > largestArea:
            largestArea = currentSum

    print("Largest Area = {}".format(largestArea))

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
        if currentPoint in coordinates:
            grid[y][x] = coordinates.index(currentPoint)
        else:
            closeCoordIdx = findClosestCoordinate(currentPoint, coordinates)
            grid[y][x] = closeCoordIdx

findLargestFiniteArea(minX, maxX, minY, maxY, coordinates, grid)