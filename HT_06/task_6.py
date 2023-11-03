""" 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву 
елементів в списку. Тобто функція приймає два аргументи: список і величину 
зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо
від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""


def shift_elements_in_the_list(input_list, shift):
    result_list = []

    for index in range(len(input_list)):
        result_list.append(input_list[index - shift % len(input_list)])
        
    return result_list


print(shift_elements_in_the_list([1, 2, 3, 4, 5], 1))
print(shift_elements_in_the_list([1, 2, 3, 4, 5], -2))
