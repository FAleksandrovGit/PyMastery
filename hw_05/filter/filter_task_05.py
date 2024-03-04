"""
5. Напишите функцию Python, которая отфильтровывает все пустые строки из списка строк с помощью функции фильтрации.
"""

string_list = ["apple", "banana", " ", "blood"]

get_no_epty = list(filter(lambda x: x.strip(),string_list))
print(get_no_epty)