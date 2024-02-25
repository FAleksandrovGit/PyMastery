def list_diff(first_list, second_list):
    #difference_list = [item for item in first_list if item not in second_list]
    diff_list = []
    for item in range(len(second_list)):
        first_list.append(second_list[item])
    for item in set(first_list):
        if item not in second_list:
            diff_list.append(item)
    return diff_list


first_test_list = [1, 2, 3, 4, 4, 2, 5, 27]
second_test_list = [5, 2, 4, 8, 25, 1, 7]
print(list_diff(first_test_list, second_test_list))
