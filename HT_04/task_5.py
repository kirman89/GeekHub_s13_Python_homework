""" 5. Create a Python program that repeatedly prompts the user
for a number until a valid integer is provided. Use a try/except
block to handle any ValueError exceptions, and keep asking for input
until a valid integer is entered. Display the final valid integer.
"""

while True:
    number = input("Enter your number: ")
    try:
        integer_number = int(number)
    except ValueError:
        print("Invalid type of input. Please, try again")
        continue
    else:
        print(f"Congratulations! Your number is {integer_number}")
        break
    