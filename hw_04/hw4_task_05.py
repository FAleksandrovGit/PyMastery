def list_diff(first_list, second_list):
    difference_list = [item for item in first_list if item not in second_list]

    return difference_list


first_test_list = [1, 2, 3, 4]
second_test_list = [5, 2, 4, 8]
print(list_diff(first_test_list, second_test_list))
