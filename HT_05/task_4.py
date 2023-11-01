""" 4. Наприклад маємо рядок : -> просто потицяв по клавi =)
--> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkow
-->     e00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
 
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка
   оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) 
    -> прiнтує довжину рядка, кiлькiсть букв та цифр

-  якщо довжина менше 30 
    -> прiнтує суму всiх чисел та окремо рядок без цифр 
    лише з буквами (без пробілів)

-  якщо довжина більше 50 
    -> щось вигадайте самі, проявіть фантазію =)
"""


def list_of_alpha(input_string):
    alpha_only = []

    for char in input_string:
        if char.isalpha():
            alpha_only.append(char)
            
    return alpha_only


def list_of_digits(input_string):
    digits_only = []

    for char in input_string:
        if char.isdigit():
            digits_only.append(int(char))

    return digits_only


def string_inspector(input_string):
    
    if 30 <= len(input_string) <= 50:
        print(f'String length is: {len(input_string)}')
        print(f'String has {len(list_of_alpha(input_string))} letters')
        print(f'String has {len(list_of_digits(input_string))} digits')

    elif len(input_string) < 30:
        print(f'Sum of numbers is: {sum(list_of_digits(input_string))}')
        print(f"String of alpha only is: {''.join(list_of_alpha(input_string))}")

    else:
        print(f"String length is: {len(input_string)} and it's too much for today :)")


string_inspector(input("Give us the best string you can! \n"))
