# 5. Write a script which accepts decimal number from user and converts it to hexadecimal.

decimal_number = int(input("Enter a decimal number:"))
hexadecimal_number = hex(decimal_number)
print(f'Hexadecimal number of {decimal_number} is {hexadecimal_number[2:]}')
