""" 5. Написати функцію <fibonacci>, яка приймає один аргумент 
і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(number):
    result = [0,]
    temp_1 = 0
    temp_2 = 1

    while temp_2 <= number:
        result.append(temp_2)
        temp_1, temp_2 = temp_2, temp_1 + temp_2

    return result


print(fibonacci(1000))
