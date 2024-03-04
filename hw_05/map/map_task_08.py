"""
8. Напишите программу на Python для преобразования заданного списка целых чисел и кортежа целых чисел в список строк.
"""

list1 = [1, 2, 3, (4, 5), 6, (7, 8, 9)]

transformed_list = list(map(lambda x: str(x), list1))
print(transformed_list)