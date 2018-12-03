import os

total = 0

# part 1
with open("./inputs/day1.txt", "r") as f:
    for line in f:
        total += int(line)

print("Part 1 - The final frequency is {}".format(total))