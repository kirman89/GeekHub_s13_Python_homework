# 4.Write a script that combines three dictionaries by updating the first one.

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

for dictionary in (dict_2, dict_3):
	dict_1.update(dictionary)

print(dict_1)
