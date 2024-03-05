"""
10. Напишите программу на Python для вычисления квадрата первых N чисел Фибоначчи с помощью функции map и создания списка этих чисел.
"""

fibbonachi_sample = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
fibo_squared = list(map(lambda x: x ** 2, fibbonachi_sample))

print(fibo_squared)