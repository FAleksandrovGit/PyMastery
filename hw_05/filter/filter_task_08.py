"""
8. Напишите программу на Python, которая создает список слов и с помощью функции фильтрации извлекает слова, содержащие более пяти букв.
"""

words_list = ["apple", "banana", "cherry", "blood", "scull", "throne"]

words_list_filtered = list(filter(lambda x: len(x) > 5, words_list))
print(words_list_filtered)