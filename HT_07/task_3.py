""" 3. На основі попередньої функції (скопіюйте кусок коду) створити 
наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів
    (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись 
    валідатором, перевірить ці дані і надрукує для кожної пари значень
    відповідне повідомлення, наприклад:

      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK

   P.S. Не забудьте використати блок try/except ;)
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
        raise ValidationException(
            "Username should not be shorter than 3 or longer than 50 letters"
            )

    if len(password) < 8 or not contain_digit(password):
        raise ValidationException('Password must contain digit & 8 symbols')

    if username.lower() in password.lower():
        raise ValidationException('Password should not contain username')

    return True


user_data_list = [
        {'username': 'Anton', 'password': 'qwerty123'},
        {'username': 'Ju', 'password': '123qwerty'},
        {'username': 'Mike', 'password': 'mike654321'},
        {'username': 'Kate', 'password': '123456789'},
        {'username': 'David', 'password': 'qwerty'},
    ]

for user in user_data_list:
    username = user['username']
    password = user['password']

    try:
        is_valid_credentials(username, password)

    except ValidationException as e:
        print(f"Name: {username}\nPassword: {password}\nStatus: {e}\n-----")

    else:
        print(f"Name: {username}\nPassword: {password}\nStatus: OK\n-----")
