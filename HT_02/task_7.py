# 7. Write a script to concatenate all elements in a list into a string and print it. 
# List must be include both strings and integers and must be hardcoded.

sample_list = ['Geek', 'Hub', '_', 'S', 13, '_', 'Pyton', '_', 2023]

print(''.join(str(el) for el in sample_list))