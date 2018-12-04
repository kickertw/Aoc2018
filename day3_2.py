import numpy as np

def get_claim(line):
    args = line.split()
    id = args[0][1:]
    pad = args[2].split(",")
    dim = args[3].split("x")
    
    left_pad = pad[0]
    top_pad = pad[1][:-1]
    width = dim[0]
    height = dim[1]

    return int(id), int(left_pad), int(top_pad), int(width), int(height)

def mark_fabric(value, id, good_list):
    if value == 0:
        return id
    
    if value in good_list:
        good_list.remove(value)
    if id in good_list:        
        good_list.remove(id)
    return -1

def init_fabric():
    fabric = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(0)
        fabric.append(row)
    return fabric

def find_id(fabric_row):
    a = np.array(fabric_row)
    unique = np.unique(a, return_counts=False)
    for i in unique:
        if i > 0:
            return i
    return 0

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1    

def main():
    fabric = init_fabric()
    good_list = list(range(1, file_len("./inputs/day3.txt") + 1))

    with open("./inputs/day3.txt", "r") as f:
        for line in f:
            id, col, row, width, height = get_claim(line)
            for i in range(width):
                for j in range(height):
                    fabric[col + i][row + j] = mark_fabric(fabric[col + i][row + j], id, good_list)
    
    print(good_list)

main()