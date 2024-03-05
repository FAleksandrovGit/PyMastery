"""
9. Напишите программу на Python для создания нового списка из определенных элементов кортежа и преобразования строкового значения в целое число.
"""

tuple1 = (1, 2, 34, 5, 6, "52", "21", 4)

transformed_tuple_to_list = list(map(int, tuple1[3:]))
print(transformed_tuple_to_list)