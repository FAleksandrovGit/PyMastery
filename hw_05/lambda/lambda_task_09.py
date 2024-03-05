"""
9. Напишите программу на Python для проверки того, является ли заданная строка числом или нет, используя лямбду.
Пример вывода:
True
True
False
True
Ложь
True
Печать контрольных чисел:
True
True
"""

sample_str1 = "Hello World!"
sample_str2 = "1112"
sample_str3 = ""

str_is_digit = lambda x: x.isdigit()
print(str_is_digit(sample_str1))
print(str_is_digit(sample_str2))
print(str_is_digit(sample_str3))