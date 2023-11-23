""" 1. Створити клас Calc, який буде мати атребут last_result та 4 
методи. Методи повинні виконувати математичні операції з 2-ма 
числами, а саме додавання, віднімання, множення, ділення.

- Якщо під час створення екземпляру класу звернутися до атребута 
last_result він повинен повернути пусте значення.

- Якщо використати один з методів - last_result повенен повернути 
результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...

- Додати документування в клас
"""


class Calc:
    '''
    A class used to perform mathematical operations.
    Have 4 methods to calculate 2 input values.
    '''

    last_result = None
    current_result = None


    def addition(self, num_1, num_2):

        self.last_result = self.current_result
        self.current_result = num_1 + num_2


    def subtraction(self, num_1, num_2):

        self.last_result = self.current_result
        self.current_result = num_1 - num_2


    def multiplication(self, num_1, num_2):

        self.last_result = self.current_result
        self.current_result = num_1 * num_2


    def division(self, num_1, num_2):

        self.last_result = self.current_result
        try:
            self.current_result = num_1 / num_2

        except ZeroDivisionError as e:
            self.current_result = e
            print(f"\n\nError: {e}")
        


calculus = Calc()
print(f"\nCurrent result: {calculus.current_result}")
print(f"Last result: {calculus.last_result}")

calculus.addition(5, 3)
print(f"\nCurrent result: {calculus.current_result}")
print(f"Last result: {calculus.last_result}")

calculus.subtraction(10, 5)
print(f"\nCurrent result: {calculus.current_result}")
print(f"Last result: {calculus.last_result}")

calculus.multiplication(5, 8)
print(f"\nCurrent result: {calculus.current_result}")
print(f"Last result: {calculus.last_result}")

calculus.division(64, 8)
print(f"\nCurrent result: {calculus.current_result}")
print(f"Last result: {calculus.last_result}")
