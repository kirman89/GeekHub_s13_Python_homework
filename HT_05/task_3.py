"""
3. Користувач вводить змiннi "x" та "y" з довiльними цифровими 
значеннями. Створiть просту умовну конструкцiю (звiсно вона 
повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися 
рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити 
ще і різницю.
Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює y"
"""

def compare_number_values(x, y):
    if x == y:
        return f'{x} equals {y}'
    if x > y:
        return f'{x} greater than {y} by {x - y}'
    else:
        return f'{y} greater than {x} by {y - x}'


x_input = input('Enter x: ')
y_input = input('Enter y: ')

try:
    x_float = float(x_input)
    y_float = float(y_input)
except ValueError:
    print('Incorrect values entered!')
else:
    print(compare_number_values(x_float, y_float))
