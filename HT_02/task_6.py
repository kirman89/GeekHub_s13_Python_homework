# 6. Write a script to check whether a value from user input is contained in a group of values.
#    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#         [1, 2, 'u', 'a', 4, True] --> 5 --> False

group_of_values = [1, 2, 'u', 'a', 4, True]
user_input = input('Please, enter your input:')

if user_input.isdigit():
	user_input = int(user_input)
elif user_input == 'True':
	user_input = True
elif user_input == 'False':
	user_input = False

if user_input in group_of_values: 
	print(True)
else:
	print(False)
