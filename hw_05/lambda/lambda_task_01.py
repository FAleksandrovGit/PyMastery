"""
1. Напишите программу на Python для создания лямбда-функции, которая прибавляет 15 к заданному числу,
переданному в качестве аргумента, а также для создания лямбда-функции, которая умножает аргумент x на аргумент y и печатает результат.
Пример вывода:
25
48
"""

plus_lambda = lambda x: x + 15
multiply_lambda = lambda x, y: x * y

put_number = int(input("Please enter a number: "))
print(f"{plus_lambda(put_number)}")

num_for_multiply1 = int(input("Please enter first number to multiply: "))
num_for_multiply2 = int(input("Please enter second number to multiply: "))
print(f"{multiply_lambda(num_for_multiply1, num_for_multiply2)}")