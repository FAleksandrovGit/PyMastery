"""
9. Напишите функцию Python, которая отфильтровывает элементы из списка строк, содержащих определенную подстроку, с помощью функции фильтрации.
"""

words_list = ["apple", "banwhiteana", "cherry", "white"]

get_word_white = list(filter(lambda x: "white" in x, words_list))
print(get_word_white)