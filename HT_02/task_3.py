# 3. Write a script which accepts a <number> from user 
# and print out a sum of the first <number> positive integers.

number = int(input("Enter a positive number:"))
sum = 0

if number > 0:
    for i in range(1, number+1):
        sum += i
    print(f'Sum of the first {number} positive integers is {sum}')
else:
    print('Number must be positive')