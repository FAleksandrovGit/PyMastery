"""
10. Напишите программу на языке Python, которая отфильтровывает даты (в формате "YYYY-MM-DD"), находящиеся в будущем, с помощью функции фильтрации
"""
from datetime import datetime

dates = ["2024-07-11", "2020-01-02", "2024-03-01"]
current_date = datetime.now()

get_future_dates = list(filter(lambda x: (datetime.strptime(x, "%Y-%m-%d") > current_date), dates))
print(get_future_dates)