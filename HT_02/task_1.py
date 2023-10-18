# 1. Write a script which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers.

str_input = input('Write a sequence of comma-separated numbers:')
number_list = list(map(int, str_input.split(',')))
number_tuple = tuple(number_list)
print(number_list)
print(number_tuple)