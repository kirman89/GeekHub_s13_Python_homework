""" 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок
і кінець діапазона, і вертатиме список простих чисел всередині цього
діапазона. Не забудьте про перевірку на валідність введених даних та у
випадку невідповідності - виведіть повідомлення.
"""


def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def prime_list(start, stop):
    result = []

    for i in range(start, stop + 1):
        if is_prime(i):
            result.append(i)

    return result


try:
    start = int(input("Enter positive integer start argument: "))
    stop = int(input("Enter positive integer stop argument: "))

except ValueError:
    print("Invalid type of input. Please, try again")

else:
    if start < 0 or stop < 0:
        raise ValueError("Arguments must be positive!")

    print(prime_list(start, stop))
