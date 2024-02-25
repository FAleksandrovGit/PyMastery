def symb_count(user_input):
    symb_list = list(user_input.lower())
    symb_dict = {key: symb_list.count(key) for key in symb_list}
    return symb_dict


input_string = input("Enter a string: ")
print(symb_count(input_string))

