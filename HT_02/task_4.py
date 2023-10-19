# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input. 
# At the end script must print out result of concatenating all <number> strings.

n = int(input("Enter a positive number:"))
result = ""

for i in range(n):
    result += input(f'{i+1}. Please, enter your input: ')
    
print(f'Result string is: {result}')