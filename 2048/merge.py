# """
# Merge function for 2048 game.
# """
#
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    non_merged_list = [0 for i in range(len(line))]
    merged_list = [0 for i in range(len(line))]
    result_list = [0 for i in range(len(line))]
    index = 0

    if 0 not in line:
        non_merged_list = line
    else:
        for i in range(len(line)):
            if line[i] != 0:
                for j in range(len(line)):
                    if non_merged_list[j] == 0:
                        non_merged_list[j] = line[i]
                        break
    print(non_merged_list)

    for num in non_merged_list:
        if index == (len(non_merged_list) - 1):
            merged_list[index] = non_merged_list[index]
        elif index > (len(non_merged_list) - 1):
            break
        elif non_merged_list[index] == non_merged_list[index + 1] and non_merged_list[index] != 0:
            merged_list[index] = (2 * non_merged_list[index])
            index += 2
            if index == len(non_merged_list):
                break
        else:
            merged_list[index] = non_merged_list[index]
            index += 1

    print(merged_list)

    for i in range(len(merged_list)):
        if merged_list[i] != 0:
            for j in range(len(merged_list)):
                if result_list[j] == 0:
                    result_list[j] = merged_list[i]
                    break

    return result_list


line = [2, 2, 0, 0]
print(merge(line))

#
# [2,0,2,4]-> [[4,4,0,0]]
# [0,0,2,2] -> [4,0,0,0]
# [2,2,0,0] ->[4,0,0,0]
# [2,2,2,2,2] -> [4,4,2,0,0]
# [8,16,16,8] -> [8,32,8,0]
