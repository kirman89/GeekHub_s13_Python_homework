"""
2. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100),
сума цифр кожного елемент якого буде дорівнювати 10.
Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]
"""


result_list = [i for i in range (100) if i % 10 + i // 10 == 10]
print(result_list)
