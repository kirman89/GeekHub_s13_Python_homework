""" 1. Write a script that will run through a list of tuples 
and replace the last value for each tuple. 
The list of tuples can be hardcoded. 
The "replacement" value is entered by user. 
The number of elements in the tuples must be different.
"""

list_of_tuples = [
	('f', True, [1, 2, 3]), 
	(), (5, 'ok', 53.9),
	(4.5, 'x', False, 'y'),
	(1, 2, 3, 4, 5)
]

replacement_value = input('Enter the replacement value: ')

for i in range(len(list_of_tuples)):
	if list_of_tuples[i]:
		list_of_tuples[i] = list_of_tuples[i][:-1] + (replacement_value,)

print(list_of_tuples)
