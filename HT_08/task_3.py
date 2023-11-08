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


def my_range(*args):

    scenarios_dict = {
        1: (0, args[0], 1),
        2: (args[0], args[1], 1),
        3: (args[0], args[1], args[2])
    }

    if len(args) in scenarios_dict.keys():
        start = scenarios_dict[len(args)][0]
        stop = scenarios_dict[len(args)][1]
        step = scenarios_dict[len(args)][2]
    
    else:
        raise TypeError('my_range function expecting from 1 to 3 arguments!')
    
    if step > 0 and start < stop:
        while start < stop:
            yield start
            start += step

    elif step < 0 and start > stop:
        while start > stop:
            yield start
            start += step

    else:
        print("You entered invalid data")


for i in my_range(1, 10, 2):
    print(i)
