""""
3. Напишите функцию Python, которая с помощью функции фильтрации отфильтровывает из списка чисел все элементы, меньшие или равные заданному значению.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


get_filtered_list = list(filter(lambda x: x <= 3,list1))
print(get_filtered_list)