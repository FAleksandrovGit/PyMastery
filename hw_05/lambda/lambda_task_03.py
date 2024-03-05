"""
3. Напишите программу на Python для сортировки списка кортежей с помощью лямбд.
Исходный список кортежей:
[('Английский язык', 88), ('Наука', 90), ('Математика', 97), ('Общественные науки', 82)].
Сортировка списка кортежей:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

sample_list = [('Английский язык', 88), ('Наука', 90), ('Математика', 97), ('Общественные науки', 82)]

get_sorted_list = lambda x: sorted(x, key=lambda y: y[1])
print(get_sorted_list(sample_list))