# 2. Write a script which accepts two sequences of comma-separated colors from user. 
# Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_input_1 = input('Write a sequence #1 of comma-separated colors:')
color_input_2 = input('Write a sequence #2 of comma-separated colors:')

color_list_1 = list(color_input_1.split(','))
color_list_2 = list(color_input_2.split(','))
result = set()

for el in color_list_1:
    if el not in color_list_2:
        result.add(el)

print(f'All colors from the first list which are not present in the 2nd list: {result}')
