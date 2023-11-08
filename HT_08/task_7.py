""" 7. Напишіть функцію, яка приймає 2 списки. Результатом має бути новий 
список, в якому знаходяться елементи першого списку, яких немає в другому.
Порядок елементів, що залишилися має відповідати порядку в першому 
(оригінальному) списку. Реалізуйте обчислення за допомогою генератора.

    Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 4, 3, 4], [2]) --> [1, 4, 3, 4]
"""


def array_diff(list_1, list_2):
    return [elem for elem in list_1 if elem not in list_2]


print(array_diff([1, 2, 2, 2, 4, 3, 4], [2]))