""" 7. Написати функцію, яка приймає на вхід список (через кому), підраховує
кількість однакових елементів у ньомy і виводить результат. Елементами списку
можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] 
    ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""

def find_unique_elements(elements_list):
    unique_elements = []
    extra_elements = []

    for elem in elements_list:
        if elem not in unique_elements:
            unique_elements.append(elem)

    for elem in elements_list:
        for unique_elem in unique_elements:
            if elem == unique_elem and type(elem) != type(unique_elem):
                extra_elements.append(elem)

    unique_elements += extra_elements

    return unique_elements


def count_elements(elements_list):
    unique_elements = find_unique_elements(elements_list)
    counted_elements = []

    for key in unique_elements:
        counter = 0

        for elem in elements_list:
            if key == elem and type(key) == type(elem):
                counter += 1

        counted_elements.append((str(key), str(counter)))

    print(',\n'.join([' -> '.join(i) for i in counted_elements]))
    

count_elements([1, 1, 'foo', [1, 2], 'foo', 1, [1, 2], True, "True", False])
