""" 5. Ну і традиційно - калькулятор :slightly_smiling_face: 
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких 
операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2,
окремо +, окремо 2; можна всі разом - типу 1 + 2). 
Операції що мають бути присутні: +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!
"""


def calculator():
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "ZeroDivisionError",
        '%': lambda x, y: x % y,
        '//': lambda x, y: x // y if y != 0 else "ZeroDivisionError",
        '**': lambda x, y: x ** y,
    }

    try:
        argument_1 = float(input("Enter first argument: "))
        operator = input("Enter operator (+, -, *, /, %, //, **): ")
        argument_2 = float(input("Enter second argument: "))

        if operator in operations:
            result = operations[operator](argument_1, argument_2)
            print(f"Result: {result}")
        else:
            print("Invalid operation")
    except ValueError:
        print("Error: incorrect value entered")


calculator()
