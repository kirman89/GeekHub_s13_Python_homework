"""
3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї 
функції. Тобто щоб її можна було використати у вигляді:

    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9

   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію
   по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
   Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(start, stop=None, step=1):

    if stop is None:
        start, stop = 0, start

    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        raise ValueError("Invalid arguments for my_range function")
    
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


for i in my_range(1, 10, 2):
    print(i)
