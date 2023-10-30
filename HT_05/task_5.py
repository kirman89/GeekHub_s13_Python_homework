""" 5. Ну і традиційно - калькулятор :slightly_smiling_face: 
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких 
операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2,
окремо +, окремо 2; можна всі разом - типу 1 + 2). 
Операції що мають бути присутні: +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!
"""

def calc(expresions):
    operations = ['+', '-', '*', '/', '%', '//', '**']
    exp_list = expresions.split(' ')

    try:
        if exp_list[1] == '+':
            return float(exp_list[0]) + float(exp_list[2])
        elif exp_list[1] == '-':
            return float(exp_list[0]) - float(exp_list[2])
        elif exp_list[1] == '*':
            return float(exp_list[0]) * float(exp_list[2])
        elif exp_list[1] == '/':
            return float(exp_list[0]) / float(exp_list[2])
        elif exp_list[1] == '%':
            return float(exp_list[0]) % float(exp_list[2])
        elif exp_list[1] == '//':
            return float(exp_list[0]) // float(exp_list[2])
        elif exp_list[1] == '**':
            return float(exp_list[0]) ** float(exp_list[2])

    except ZeroDivisionError:
        print("Zero division error! Change value or operator")
        return False

    except ValueError:
        print("Incorrect input! Check your value and operator")
        return False

expr_input = input("Enter expresion in format 'arg1 operator arg2':\n")
print(calc(expr_input))
