import os

def check_freq(str):
    freq = {}

    for c in str:
        if (c not in freq):
            freq[c] = str.count(c)
    return freq

def get_mini_checksum(letter_freq):
    a = 0
    b = 0
    for key, value in letter_freq.items():
        if a == 1 and b == 1:
            return a, b
        if value == 2:
            a = 1
        if value == 3:
            b = 1        
    return a, b

checksum_a = 0
checksum_b = 0

# part 1
with open("./inputs/day2.txt", "r") as f:
    for line in f:
        a = 0
        b = 0
        line_freq = check_freq(line)
        a, b = get_mini_checksum(line_freq)
        checksum_a += a
        checksum_b += b

final = checksum_a * checksum_b
print("Checksum = {}".format(final)) 