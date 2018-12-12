def findManhattenDistance(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

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

