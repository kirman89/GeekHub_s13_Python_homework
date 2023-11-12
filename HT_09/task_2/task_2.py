""" 
2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та 
кількість символів. Файл також додайте в репозиторій. На екран повинен
вивестись список із трьома блоками - символи з початку, із середини 
та з кінця файлу. Кількість символів в блоках - та, яка введена в
другому параметрі. 

Придумайте самі, як обробляти помилку, наприклад, коли кількість 
символів більша, ніж є в файлі або, наприклад, файл із двох символів 
і треба вивести по одному символу, то що виводити на місці середнього 
блоку символів?). 

Не забудьте додати перевірку чи файл існує.
"""


from os import path


def text_block_slicer(filename, length_of_block):

    try:
        if not path.exists(filename):
            raise FileNotFoundError

    except FileNotFoundError:
        print('File does not exist')

    else:
        with open(filename, 'rt') as file:
            text = file.read()

        if length_of_block > len(text) / 3:
            print(f"Text content of the file {filename} "
                  f"is not enough to form blocks!")

        else:
            first_block = text[:length_of_block]
            third_block = text[-length_of_block:]

            second_block = text[int(len(text) / 2 - length_of_block / 2)
                :int(len(text) / 2 + length_of_block / 2)]

            print([first_block, second_block, third_block])


for i in range(1, 8):
    text_block_slicer('task_2.txt', i)
