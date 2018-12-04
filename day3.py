import numpy as np

def get_claim(line):
    args = line.split()
    pad = args[2].split(",")
    dim = args[3].split("x")
    
    left_pad = pad[0]
    top_pad = pad[1][:-1]
    width = dim[0]
    height = dim[1]

    return int(left_pad), int(top_pad), int(width), int(height)

def mark_fabric(value):
    if value == 0:
        return 1
    if value >= 1:
        return 2

def init_fabric():
    fabric = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(0)
        fabric.append(row)
    return fabric

def count_overlap(fabric_row):
    a = np.array(fabric_row)
    unique, counts = np.unique(a, return_counts=True)
    counts = dict(zip(unique, counts))
    
    return counts[2] if 2 in counts else 0

def main():
    fabric = init_fabric()
    with open("./inputs/day3.txt", "r") as f:
        for line in f:
            col, row, width, height = get_claim(line)
            for i in range(width):
                for j in range(height):
                    fabric[col + i][row + j] = mark_fabric(fabric[col + i][row + j])

    overlap_count = 0
    for i in range(1000):
        overlap_count += count_overlap(fabric[i])
    
    print("Overlap Count = {}".format(overlap_count))

main()