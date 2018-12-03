import os

total = 0
repeatNotFound = True
rf = set()


# part 2
while repeatNotFound:
    with open("./inputs/day1.txt", "r") as f:
        for line in f:
            if total not in rf:
                rf.update([total])
                total += int(line)     
            else:
                print("Part 2 - The 1st repeating frequency is {}".format(total))
                repeatNotFound = False
                break