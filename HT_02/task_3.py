# 3. Write a script which accepts a <number> from user 
# and print out a sum of the first <number> positive integers.

number = int(input("Enter a positive number:"))
result_sum = 0

if number > 0:
    for i in range(1, number+1):
        result_sum += i
    print(f'Sum of the first {number} positive integers is {result_sum}')
else:
    print('Number must be positive')
    