""" 1. Створіть функцію, всередині якої будуть записано список із п'яти
користувачів (ім'я та пароль). Функція повинна приймати три аргументи:
два - обов'язкових (<username> та <password>) і третій - необов'язковий
параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення
        LoginException (його також треба створити =))
"""


class LoginException(Exception):
    pass


def is_valid_credentials(username, password, silent=False):

    users_list = [
        {'username': 'Anton', 'password': 'qwerty123'},
        {'username': 'Julia', 'password': '123qwerty'},
        {'username': 'Mike', 'password': '654321'},
        {'username': 'Kate', 'password': '123456'},
        {'username': 'David', 'password': 'qwerty123'},
    ]
        
    for user in users_list:
        if user['username'] == username and user['password'] == password:
            return True

    if silent:
        return False
    else:
        raise LoginException('You entered invalid credentials')


try:
    print(is_valid_credentials('Anton', 'qwerty123'))
    print(is_valid_credentials('Mike', 'qwerty123', True))
    print(is_valid_credentials('Mike', 'qwerty123'))

except LoginException as e:
    print(e)
