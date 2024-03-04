"""
2. Напишите программу на Python для создания функции, которая принимает один аргумент, и этот аргумент будет умножен на неизвестное заданное число.
Пример вывода:
Удвоить число 15 = 30
Утроить число 15 = 45
Четырехкратное число 15 = 60
Удвоить число 15 = 75
"""

multiply = lambda x, y: x * y
sample_number = int(input("Enter the number: "))
print(f"Doubled: {multiply(sample_number, 2)}")
print(f"Tripled: {multiply(sample_number, 3)}")
print(f"4 times bigger: {multiply(sample_number, 4)}")