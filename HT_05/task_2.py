""" 2. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй
повинна повертати якийсь результат (напр. інпут від юзера, результат
математичної операції тощо). Також створiть четверту ф-цiю, яка
всередині викликає 3 попереднi, обробляє їх результат та також
повертає результат своєї роботи. Таким чином ми будемо викликати
одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
"""

def consist_of_valid_chars(phone_number):
    valid_chars = '0123456789'
    for char in phone_number:
        if char not in valid_chars:
            return False
    return True

def starts_with_valid_numbers(phone_number):
    operators = (
        "050", "066", "095",
        "099", "063", "073",
        "093", "067", "096",
        "097", "098", "068"
    )
    for operator in operators:
        if phone_number.startswith(operator):
            return True
    return False

def have_valid_lenght(phone_number):
    if len(phone_number) == 10:
        return True
    else:
        return False

def is_phone_number_valid(phone_number):
    if (have_valid_lenght(phone_number) and 
        starts_with_valid_numbers(phone_number) and
        consist_of_valid_chars(phone_number)):
        #Check all three conditions
        return True
    else:
        return False


print(is_phone_number_valid(input("Enter phone number. Format 0XXXXXXXXX:")))
