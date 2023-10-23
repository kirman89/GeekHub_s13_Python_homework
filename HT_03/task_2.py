""" 2. Write a script to remove an empty elements from a list. 
Test list: 
[(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
"""

test_list = [
	(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []
]
result_list = []

for elem in test_list:
	if elem:
		result_list.append(elem)

print(f'Test list: {test_list}')
print(f'Rslt list: {result_list}')
