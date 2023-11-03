""" 7. Написати функцію, яка приймає на вхід список (через кому), підраховує
кількість однакових елементів у ньомy і виводить результат. Елементами списку
можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] 
    ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""


def count_elements(elements_list):
    frequency = {}

    for element in elements_list:
        key = element if not isinstance(element, list) else str(element)
        
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1

    for element, count in frequency.items():
        print(f"{element} -> {count}")


count_elements([1, '1', 'foo', [1, 2], 'foo', 1, [1, 2], True, "True", None, "None", False, "False"])

