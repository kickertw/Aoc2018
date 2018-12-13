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


def grid_init(width, height):
    grid = [None] * height
    for i in range(height):
        grid[i] = [None] * width

    return grid

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

print("{},{}".format(maxX, maxY))
grid = grid_init(maxX + 1, maxY + 1)

for i in range(maxX):
    for j in range(maxY):
        currentPoint = (i, j)
        closeCoordIdx = findClosestCoordinate(currentPoint, coordinates)
        print("{},{}".format(i,j))
        grid[i][j] = closeCoordIdx

print(grid)