"""
1. Напишите функцию Python, которая отфильтровывает четные числа из списка целых чисел с помощью функции filter.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_list = list(filter(lambda x: x % 2 == 0, list1))
print(filtered_list)