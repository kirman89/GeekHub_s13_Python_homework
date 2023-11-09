""" 5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість 
окремих регістро-незалежних букв та цифр, які зустрічаються в рядку 
більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих 
і малих). Реалізуйте обчислення за допомогою генератора.

    Example (input string -> result):
    
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі
"""


#def counter_of_repeating_values(input_string):
#    return len(set([val for val in input_string.upper() if input_string.upper().count(val) > 1]))


def counter_of_repeating_values(input_string):
    char_count_dict = {}

    def get_next_char(input_string):
        for char in input_string:
            yield char.lower()

    chars = get_next_char(input_string)

    while True:
        try:
            current_char = next(chars)
            if current_char in char_count_dict.keys():
                char_count_dict[current_char] += 1
            else:
                char_count_dict[current_char] = 1

        except:
            counter = 0
            for value in char_count_dict.values():
                if value > 1:
                    counter += 1

            return counter


print(counter_of_repeating_values("abcde"))
print(counter_of_repeating_values("aabbcde"))
print(counter_of_repeating_values("aabBcde"))
print(counter_of_repeating_values("indivisibility"))
print(counter_of_repeating_values("Indivisibilities"))
print(counter_of_repeating_values("aA11"))
print(counter_of_repeating_values("ABBbbddddddbbbbA"))
