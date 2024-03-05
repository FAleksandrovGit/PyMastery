"""
8. Напишите программу на Python для извлечения года, месяца, даты и времени с помощью Lambda.
Пример вывода:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""
from datetime import datetime

get_date = lambda: f'{datetime.now()}\n{datetime.now().year}\n{datetime.now().month}\n{datetime.now().day}\n{datetime.now().time()}'
print(get_date())
