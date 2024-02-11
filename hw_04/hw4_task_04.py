def rev_dict(input_dict):
    rever_input_dict = {value: key for key, value in input_dict.items()}
    return rever_input_dict


test_dict = {"a": 1, "B": 2, 3: "C"}
print(rev_dict(test_dict))
