# 6. Write a script to get the maximum and minimum value in a dictionary.

my_dict = {
    'id': 17,
    'name': 'NoName',
    'freeze': -35,
    'count': 1,
    'admin': False,
    'errors': [400, 403],
    'email': None,
    'salary': 3750,
    'speed': 75.8,
    'file': 100644,
}

numeric_values = []

for value in my_dict.values():
    if isinstance(value, (int, float)):
        numeric_values.append(value)

print(f'Min value: {min(numeric_values)}')
print(f'Max value: {max(numeric_values)}')
