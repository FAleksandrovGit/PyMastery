"""
4. Напишите программу на Python, которая создает список имен и с помощью функции фильтрации извлекает имена, начинающиеся с гласной буквы (A, E, I, O, U).
"""

names = ['Alice', 'Bob', 'Charlie', 'Zhora', 'Ivy']
vocals = ("A", "E", "I", "O", "U")

get_names = list(filter(lambda x: x.startswith(vocals), names))
print(get_names)