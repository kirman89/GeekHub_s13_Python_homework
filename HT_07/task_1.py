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
    users = {
        'username1':'password1',
        'username2':'password2',
        'username3':'password3',
        'username4':'password4',
        'username5':'password5'
    }

    if username in users.keys() and users[username] == password:
        return True

    if silent:
        return False
    else:
        raise LoginException('You entered invalid credentials')


try:
    print(is_valid_credentials('username3', 'password3'))
    print(is_valid_credentials('username', 'password', True))
    print(is_valid_credentials('username', 'password'))

except LoginException as e:
    print(e)
