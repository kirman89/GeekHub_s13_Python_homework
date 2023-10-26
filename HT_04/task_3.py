"""
3. Create a Python script that takes an age as input.
If the age is less than 18 or greater than 120, raise a custom
exception called InvalidAgeError. Handle the InvalidAgeError by 
displaying an appropriate error message.
"""

class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter valid age: "))
    if not 18 <= age <= 120:
        raise InvalidAgeError("This age is not valid!")
except InvalidAgeError as e:
    print(f'Error: {e}')
except ValueError:
    print("Error: Please enter a valid input")
else:
    print("This age is valid!!")
