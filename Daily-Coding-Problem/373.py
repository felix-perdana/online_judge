def find_max_consecutive_length(lst):
    dict = {}
    max_distance = -1

    for num in lst:
        right_border = num+1
        left_border = num-1
        dict[num] = {}
        dict[num]['right_border'] = num
        dict[num]['left_border'] = num
        if dict.get(right_border) != None:
            dict[num]['right_border'] = dict[right_border]['right_border']
        if dict.get(left_border) != None:
            dict[num]['left_border'] = dict[left_border]['left_border']

        dict[dict[num]['right_border']]['left_border'] = dict[num]['left_border']
        dict[dict[num]['left_border']]['right_border'] = dict[num]['right_border']

        distance = dict[num]['right_border'] - dict[num]['left_border'] + 1
        print(str(num) + '=>' + str(dict[num]['right_border']) + ';' + str(dict[num]['left_border']))
        max_distance = max(distance, max_distance)

    return max_distance

print(find_max_consecutive_length([5, 2, 99, 3, 4, 1, 100]))
print(find_max_consecutive_length([3, 5, 1, 6, 4, 0, 2, 3]))
print(find_max_consecutive_length([-4, 8, 5, 7, 6]))
