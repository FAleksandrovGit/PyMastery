"""
7. Напишите программу на Python, которая отфильтровывает простые числа из списка целых чисел с помощью функции filter.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

get_prime_num = list(filter(lambda x: (x % 2 != 0 and x != 1 or x == 2), list1))
print(get_prime_num)