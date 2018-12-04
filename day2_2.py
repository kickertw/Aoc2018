box_list = []

def is_close_match(word1, word2):
    ii = 0
    lw1 = list(word1)
    lw2 = list(word2)

    diff_count = 0
    for i in range(len(word1)):
        if lw1[i] != lw2[i]:
            diff_count += 1
            ii = i
        if diff_count > 1:
            return False, ""
    return True, lw1[:ii] + lw1[ii+1:]

with open("./inputs/day2.txt", "r") as f:
    for line in f:
        box_list.append(line)

    for ii in range(len(box_list)):
        key = box_list[ii]
        for jj in range(ii+1, len(box_list)):
            isValid, common_letters = is_close_match(key, box_list[jj])
            if isValid:
                print(common_letters)
