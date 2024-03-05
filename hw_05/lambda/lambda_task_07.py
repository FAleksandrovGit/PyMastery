"""
7. Напишите программу на языке Python, чтобы найти, начинается ли заданная строка с заданного символа, используя лямбду.
Пример вывода:
True
False
"""

check_str = lambda x: x.lower().startswith('a') # Если хочется чекнуть именно на саму букву без учета регистра, чтобы учитывать регистр уберите .lower()
sample_str = input("Enter a string: ")
print(check_str(sample_str))