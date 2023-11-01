""" 1. Написати функцію <square>, яка прийматиме один аргумент - сторону
квадрата, і вертатиме 3 значення у вигляді кортежа: периметр квадрата,
площа квадрата та його діагональ.
"""


def square(side):
    return 4 * side, side ** 2, round((2 ** 0.5) * side, 2)


print(square(int(input("Enter the side length of square: "))))
