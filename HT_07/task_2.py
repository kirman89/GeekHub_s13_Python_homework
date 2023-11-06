""" 
2. Створіть ф. для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати 
   хоча б одну цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити
   виключення із відповідним текстом.
"""


class ValidationException(Exception):
    pass


def contain_digit(password):

    for char in password:
        if char.isdigit():
            return True

    return False


def is_valid_credentials(username, password):

    if not 3 <= len(username) <= 50:
        raise ValidationException('Username has incorrect length')

    if len(password) < 8 or not contain_digit(password):
        raise ValidationException('Password must contain digit & 8 symbols')

    if username.lower() in password.lower():
        raise ValidationException('Password should not contain username')

    return True


username = input('Enter username: ')
password = input('Enter username: ')

try:
    if is_valid_credentials(username, password):
        print('Credentials are valid')

except ValidationException as e:
    print(e)
