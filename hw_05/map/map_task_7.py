"""
7. Напишите программу на Python, чтобы сложить два заданных списка и найти разницу между ними. Используйте функцию map().
"""


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]

sum_list = list(map(lambda x, y: x + y, list1, list2))
substraction_list = list(map(lambda x, y: x - y, list1, list2))
print(sum_list)
print(substraction_list)