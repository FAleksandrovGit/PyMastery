def to_dict(user_list):
    new_dict = {user_list[i]: user_list[i] for i in range(len(user_list))}
    return new_dict


list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(to_dict(list_test))
