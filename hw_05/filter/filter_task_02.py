"""
2. Напишите программу на Python, которая с помощью функции filter извлекает все заглавные буквы из списка строк со смешанным регистром
"""

list1 = ["W", "s", "A4s", "p", "51G35133FF"]

only_capital = list(filter(lambda x: x.isupper(), "".join(list1)))
print(only_capital)