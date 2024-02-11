def stud_avg(stud_dict):
    average_points = sum(stud_dict.values()) / len(stud_dict)
    bests = {key: value for key, value in stud_dict.items() if value > average_points}
    return bests.keys()


test_dict = {"Aleksandr Bad": 90, "Galaxy Squad": 14, "Bobby Clown": 75}

print(stud_avg(test_dict))
