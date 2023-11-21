""" Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких
    файлів. Якщо в попередньому завданні ви добре продумали структуру 
    програми то у вас не виникне проблем швидко адаптувати її до 
    нових вимог.

    - на старті додати можливість залогінитися або створити новго
    користувача (при створенні новго користувача, перевіряється 
    відповідність логіну і паролю мінімальним вимогам. Для перевірки 
    створіть окремі функції)

    - в таблиці (базі) з користувачами має бути створений унікальний 
    користувач-інкасатор, який матиме розширені можливості (домовимось,
    що логін/пароль будуть admin/admin щоб було простіше перевіряти)
    
    - банкомат має власний баланс
    
    - кількість купюр в банкоматі обмежена. 
    Номінали купюр - 10, 20, 50, 100, 200, 500, 1000

    - змінювати вручну кількість купюр або подивитися їх залишок в 
    банкоматі може лише інкасатор

    - користувач через банкомат може покласти на рахунок лише сумму 
    кратну мінімальному номіналу що підтримує банкомат. В іншому 
    випадку - повернути "здачу" 
    (наприклад при поклажі 1005 --> повернути 5). 
    Але це не має впливати на баланс/кількість купюр банкомату, 
    лише збільшуєтсья баланс користувача (моделюємо наявність двох 
    незалежних касет в банкоматі - одна на прийом, інша на видачу)

    - зняти можна лише в межах власного балансу, але не більше ніж є 
    всього в банкоматі.
    
    - при неможливості виконання якоїсь операції - вивести 
    повідомлення з причиною (не вірний логін/пароль, недостатньо 
    коштів на раунку, неможливо видати суму наявними купюрами тощо.)
"""


from datetime import datetime
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).parent
DB_PATH = Path(BASE_DIR, "atm.db")


def create_connection(db_file):
    connection = None

    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to db")
        return connection

    except Exception as e:
        print("Error while working with SQLite3", e)

    return connection


def close_connection(connection):

    if connection:
        connection.close()
        print("Connection closed")


def display_menu():
    print("\n\nMenu:\n1. Check balance\n2. Deposit money")
    print("3. Withdraw money\n4. End session")


def display_admin_menu():
    display_menu()
    print("\nAdmin Menu:\n5. Check atm balance\n6. Change atm balance")


def login(connection):
    max_attempts = 3
    current_attempt = 0

    while current_attempt < max_attempts:
        username = input("\nEnter username: ")
        password = input("Enter password: ")

        if is_correct_credentials(connection, username, password):
            print(f"\nWelcome, {username}!")
            start_atm_actions(connection, username)
            return True

        print("Credentials are not valid. Try again.")
        current_attempt += 1

    print("You have reached the limit of attempts. Go to start menu")
    return False


def is_correct_credentials(connection, username, password):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM users 
        WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()

    if user is None:
        return False

    return True


def is_user_admin(connection, username):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT is_admin FROM users
        WHERE username=?
    """, (username,))

    result = cursor.fetchone()

    if result[0] == 1:
        return True

    return False


def display_balance(balance):
    print(f"\nCurrent balance: {balance} UAH")


def check_balance(connection, username):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT balance 
        FROM user_balance AS us_b
        JOIN users AS u
        ON us_b.user_id=u.id
        WHERE username=?
    """, (username,))

    result = cursor.fetchone()

    if result is None:
        balance = 0
    else:
        balance = result[0]

    return balance


def update_balance(connection, username, new_balance):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id 
        FROM users
        WHERE username=?
    """, (username,))

    user_id = cursor.fetchone()[0]

    cursor.execute("""
        UPDATE user_balance 
        SET balance=?, last_update=?
        WHERE user_id=?
    """, (new_balance, datetime.now(), user_id))

    connection.commit()


def add_transaction(connection, username, transaction_type, transaction_amount):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id 
        FROM users
        WHERE username=?
    """, (username,))

    user_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO transactions (user_id, transaction_type, transaction_amount) 
        VALUES (?, ?, ?)
    """, (user_id, transaction_type, transaction_amount))

    connection.commit()


def is_valid_amount(user_input):
    try:
        amount = int(user_input)
    except ValueError:
        print("You entered invalid amount!")
        return False
    else:
        return amount > 0


def deposit_money(connection, username):

    balance = check_balance(connection, username)
    user_input = input("\nEnter the amount you want to deposit: ")

    if is_valid_amount(user_input):
        amount = int(user_input)
        change_amount = amount % 10

        if change_amount != 0:
            amount -= change_amount
            print(f"\nBalance was replenished by {amount} UAH.")
            print(f"{change_amount} UAH returned.")
        else:
            print(f"\nBalance was replenished by {amount} UAH.")

        balance += amount

        update_balance(connection, username, balance)
        add_transaction(connection, username, 'deposit_money', amount)
        display_balance(balance)

    else:
        print("You entered invalid amount!")
        return


def withdraw_money(connection, username):

    user_input = input("\nEnter the amount you want to withdraw: ")

    if is_valid_amount(user_input):
        amount = int(user_input)

        if amount > check_atm_balance_sum(connection, username):
            print("Not enough funds in the ATM. Try a smaller amount.")
            return

        else:
            balance = check_balance(connection, username)

            if amount > balance:
                print("Insufficient funds to withdraw. Try a smaller amount.")
                return

            else:
                balance -= amount

                update_balance(connection, username, balance)
                add_transaction(connection, username, 'withdraw_money', amount)

                print(f"\nThe {amount} UAH was withdrawn from the balance.")
                display_balance(balance)

    else:
        print("You entered invalid amount!")
        return


def register_new_user(connection):
    print("\nUser must be unique and credentials at least 5 characters long.")

    username = input("Enter username of new user: ")

    if user_exists(connection, username):
        print("Error, the entered user already exists")
        return

    password = input("Enter password of new user: ")

    if not is_valid_credentials(username, password):
        print("Credentials must be at least 5 characters long.")
    else:
        insert_new_user_to_db(connection, username, password)
        print("\nNew user has been added to DB.")


def insert_new_user_to_db(connection, username, password):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (username, password, is_admin) 
        VALUES (?, ?, 0)
    """, (username, password))

    connection.commit()


def user_exists(connection, username):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT username 
        FROM users
        WHERE username=?
    """, (username,))

    result = cursor.fetchone()

    return result is not None and len(result) > 0


def is_valid_credentials(username, password):
    return len(username) >= 5 and len(password) >= 5


def check_atm_balance(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * 
        FROM atm_balance
    """)

    result = cursor.fetchall()
    print("\n\nBanknote balance in the ATM: ")

    for banknote in result:
        print(f"Nominal {banknote[0]} UAH - current amount {banknote[1]}")

    print(f"Total ATM balance is: {check_atm_balance_sum(connection)} UAH.")


def check_atm_balance_sum(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT sum(nominal * count)
        FROM atm_balance
    """)

    result = cursor.fetchone()

    return result[0]


def change_atm_balance(connection):
    print("\nAvailable denominations: 10, 20, 50, 100, 200, 500, 1000")
    nominal = input("\nEnter denomination to change: ")

    if nominal in ("10", "20", "50", "100", "200", "500", "1000"):
        banknote_amount = input("Enter amount of banknotes: ")

        if is_valid_amount(banknote_amount):
            change_atm_banknote_balance(connection, nominal, banknote_amount)
        else:
            print("You entered invalid amount!")
            return

    else:
        print("You entered incorrect nominal!")
        return


def change_atm_banknote_balance(connection, nominal, banknote_amount):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE atm_balance
        SET count=?
        WHERE nominal=? 
    """, (banknote_amount, nominal))

    connection.commit()


def start_atm_actions(connection, username):
    is_admin = is_user_admin(connection, username)

    while True:
        if is_admin:
            display_admin_menu()
            user_choice = input(f"{'-'*10}\nChoose an action (1-6): ")

        else:
            display_menu()
            user_choice = input(f"{'-'*10}\nChoose an action (1-4): ")

        if user_choice == '1':
            display_balance(check_balance(connection, username))

        elif user_choice == '2':
            deposit_money(connection, username)

        elif user_choice == '3':
            withdraw_money(connection, username)

        elif user_choice == '4':
            print("Have a nice day!")
            close_connection(connection)
            return

        elif user_choice == '5' and is_admin:
            check_atm_balance(connection)

        elif user_choice == '6' and is_admin:
            change_atm_balance(connection)

        else:
            print("Incorrect input. Try again.")


def start():
    connection = create_connection(DB_PATH)

    while True:
        print("\n\nChoose the option:\n1. Log in\n2. Sign up\n3. Exit")
        chosen_option = input(f"{'-'*10}\nOption (1-3): ")

        if chosen_option == '1':

            if login(connection):
                close_connection(connection)
                return

        elif chosen_option == '2':
            register_new_user(connection)

        elif chosen_option == '3':
            print("Have a nice day!")
            close_connection(connection)
            return

        else:
            print("Incorrect input. Try again.")


start()
