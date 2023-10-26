""" 1. Написати скрипт, який приймає від користувача два числа 
(int або float) і робить наступне:
    a. Кожне введене значення спочатку пробує перевести в int. 
У разі помилки - пробує перевести в float, а якщо і там ловить помилку
- пропонує ввести значення ще раз (зручніше на даному етапі навчання 
для цього використати цикл while)
    b. Виводить результат ділення першого на друге. 
Якщо виникає помилка - оброблює її і виводить відповідне повідомлення
"""

while True:
    number_1 = input("Enter your first number: ")
    number_2 = input("Enter your second number: ")

    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        try:
            number_1 = float(number_1)
            number_2 = float(number_2)
        except ValueError:
            print("Invalid type of input. Please, try again")
            continue
        else:
            break
    else:
        break

try:
    print(f'Result of division = {number_1 / float(number_2)}')
except Exception as e:
    print("Error", str(e))
