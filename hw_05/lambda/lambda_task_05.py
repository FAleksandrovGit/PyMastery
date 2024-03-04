"""
5. Напишите программу на Python для фильтрации списка целых чисел с помощью лямбды.
Исходный список целых чисел:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Четные числа из указанного списка:
[2, 4, 6, 8, 10]
Нечетные числа из указанного списка:
[1, 3, 5, 7, 9]
"""

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

only_even = list(filter(lambda x: x % 2 == 0, sample_list))
only_odd = list(filter(lambda x: x % 2 != 0, sample_list))

print(f"Only even numbers: {only_even} \nOnly odd numbers: {only_odd}")