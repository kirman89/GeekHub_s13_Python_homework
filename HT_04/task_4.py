""" 4. Write a Python program that demonstrates exception chaining.
Create a custom exception class called CustomError and another
called SpecificError. In your program (could contain any logic
you want), raise a SpecificError, and then catch it in a try/except
block, re-raise it as a CustomError with the original exception
as the cause. Display both the custom error message and the original
exception message.
"""

class CustomError(Exception):
    pass

class SpecificError(Exception):
    pass

try:
    raise SpecificError("The original SpecificError")

except SpecificError as original_exception:
    try:
        raise CustomError("CustomError with the cause") from original_exception
    except CustomError as custom_exception:
        print(f"CustomError message: {custom_exception}")
        print(f"Original SpecificError message: {original_exception}")
