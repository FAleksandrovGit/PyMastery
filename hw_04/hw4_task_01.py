def to_dict(lst):
    new_dict = {lst[i]: lst[i] for i in range(len(lst))}
    return new_dict


list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(to_dict(list_test))
