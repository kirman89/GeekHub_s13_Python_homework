""" 2. Create a custom exception class called NegativeValueError.
Write a Python program that takes an integer as input and raises 
the NegativeValueError if the input is negative. Handle this custom 
exception with a try/except block and display an error message.
"""

class NegativeValueError(Exception):
	pass


try:
	integer_input = int(input("Enter positive integer: "))
	if integer_input < 0:
		raise NegativeValueError("Negative input is not allowed!")
except NegativeValueError as e:
	print(f'Error: {e}')
except ValueError:
    print("Error: Please enter a valid input")
else:
	print("Congratulations!")
	