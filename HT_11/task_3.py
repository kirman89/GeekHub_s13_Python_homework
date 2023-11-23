""" 3. Банкомат 2.0: переробіть программу з функціонального підходу 
програмування на використання класів. Додайте шанс 10% отримати 
бонус на баланс при створенні нового користувача.
"""


from datetime import datetime
import sqlite3
from pathlib import Path
import random


BASE_DIR = Path(__file__).parent
DB_PATH = Path(BASE_DIR, "atm.db")


class ATM:

    def __init__(self, path):
        self.database = Database(path)


    def start(self):
        self.database.create_atm_db()

        while True:
            print("\n\nChoose the option:\n1. Log in\n2. Sign up\n3. Exit")
            chosen_option = input(f"{'-'*10}\nOption (1-3): ")

            if chosen_option == '1':

                if self.login():
                    self.database.close_connection_to_db()
                    return

            elif chosen_option == '2':
                self.register_new_user()

            elif chosen_option == '3':
                print("Have a nice day!")
                self.database.close_connection_to_db()
                return

            else:
                print("Incorrect input. Try again.")


    def login(self):
        max_attempts = 3
        current_attempt = 0

        while current_attempt < max_attempts:
            username = input("\nEnter username: ")
            password = input("Enter password: ")

            if self.database.is_correct_credentials(username, password):
                print(f"\nWelcome, {username}!")
                self.start_atm_actions(username)
                return True

            print("Credentials are not valid. Try again.")
            current_attempt += 1

        print("You have reached the limit of attempts. Go to start menu")
        return False


    def is_lucky(self):
        return random.random() <= 0.1


    def register_new_user(self):
        print("\nUser must be unique and credentials at least 5 characters long.")

        username = input("Enter username of new user: ")
        if not self.is_valid_credential(username):
            print("Username must be at least 5 characters long.")
            return

        if self.database.user_exists(username):
            print("Error, the entered user already exists")
            return

        password = input("Enter password of new user: ")

        if not self.is_valid_credential(password):
            print("Password must be at least 5 characters long.")
        else:
            self.database.insert_new_user_to_db(username, password)
            print("\nNew user has been added to DB.")

            if self.is_lucky():
                print("\n\nCongratulations! You received a bonus of 100 UAH")
                self.database.insert_initial_balance_sum(username, 100)

            else:
                self.database.insert_initial_balance_sum(username, 0)


    def check_atm_balance(self):
        result = self.database.get_atm_balance()
        print("\n\nBanknote balance in the ATM: ")

        for banknote in result:
            print(f"Nominal {banknote[0]} UAH - current amount {banknote[1]}")

        print(f"Total ATM balance is: {self.database.check_atm_balance_sum()} UAH.")


    def change_atm_balance(self):
        print("\nAvailable denominations: 10, 20, 50, 100, 200, 500, 1000")
        nominal = input("\nEnter denomination to change: ")

        if nominal in ("10", "20", "50", "100", "200", "500", "1000"):
            banknote_amount = input("Enter amount of banknotes: ")

            if self.is_valid_amount(banknote_amount):
                self.database.change_atm_banknote_balance(nominal, banknote_amount)
            else:
                print("You entered invalid amount!")
                return

        else:
            print("You entered incorrect nominal!")
            return


    def display_menu(self):
        print("\n\nMenu:\n1. Check balance\n2. Deposit money")
        print("3. Withdraw money\n4. End session")


    def display_admin_menu(self):
        self.display_menu()
        print("\nAdmin Menu:\n5. Check atm balance\n6. Change atm balance")


    def display_balance(self, balance):
        print(f"\nCurrent balance: {balance} UAH")


    def is_valid_credential(self, credential):
        return len(credential) >= 5


    def is_valid_amount(self, user_input):
        try:
            amount = int(user_input)
        except ValueError:
            print("You entered invalid amount!")
            return False
        else:
            return amount > 0


    def start_atm_actions(self, username):
        is_admin = self.database.is_user_admin(username)

        while True:
            if is_admin:
                self.display_admin_menu()
                user_choice = input(f"{'-'*10}\nChoose an action (1-6): ")

            else:
                self.display_menu()
                user_choice = input(f"{'-'*10}\nChoose an action (1-4): ")

            if user_choice == '1':
                self.display_balance(self.database.check_balance(username))

            elif user_choice == '2':
                self.deposit_money(username)

            elif user_choice == '3':
                self.withdraw_money(username)

            elif user_choice == '4':
                print("Have a nice day!")
                return

            elif user_choice == '5' and is_admin:
                self.check_atm_balance()

            elif user_choice == '6' and is_admin:
                self.change_atm_balance()

            else:
                print("Incorrect input. Try again.")


    def deposit_money(self, username):

        balance = self.database.check_balance(username)
        user_input = input("\nEnter the amount you want to deposit: ")

        if self.is_valid_amount(user_input):
            amount = int(user_input)
            change_amount = amount % 10

            if change_amount != 0:
                amount -= change_amount
                print(f"\nBalance was replenished by {amount} UAH.")
                print(f"{change_amount} UAH returned.")
            else:
                print(f"\nBalance was replenished by {amount} UAH.")

            balance += amount

            self.database.update_balance(username, balance)
            self.database.add_transaction(username, 'deposit_money', amount)
            self.display_balance(balance)

        else:
            print("You entered invalid amount!")
            return


    def withdraw_money(self, username):

        user_input = input("\nEnter the amount you want to withdraw: ")

        if self.is_valid_amount(user_input):
            amount = int(user_input)

            if amount > self.database.check_atm_balance_sum():
                print("Not enough funds in the ATM. Try a smaller amount.")
                return

            else:
                balance = self.database.check_balance(username)

                if amount > balance:
                    print("Insufficient funds to withdraw. Try a smaller amount.")
                    return

                else:
                    balance -= amount

                    self.database.update_balance(username, balance)
                    self.database.add_transaction(username, 'withdraw_money', amount)

                    print(f"\nThe {amount} UAH was withdrawn from the balance.")
                    self.display_balance(balance)

        else:
            print("You entered invalid amount!")
            return


class Database:

    def __init__(self, path):
        self.connection = sqlite3.connect(path)


    def create_atm_db(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                is_admin INTEGER NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_balance(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                balance INTEGER NOT NULL,
                last_update DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                transaction_amount INTEGER NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atm_balance(
                nominal INTEGER PRIMARY KEY,
                count INTEGER
            )
        """)

        users = [
            ('1', 'admin', 'admin', '1'),
            ('2', 'user1', 'password1', '0'),
            ('3', 'user2', 'password2', '0')
        ]

        bills = [
            (10, 100),
            (20, 100),
            (50, 100),
            (100, 50),
            (200, 50),
            (500, 50),
            (1000, 10)
        ]

        cursor.executemany("INSERT OR IGNORE INTO users VALUES (?,?,?,?)", users)
        cursor.executemany("INSERT OR IGNORE INTO atm_balance VALUES (?,?)", bills)

        cursor.execute("""
            INSERT OR IGNORE INTO user_balance (user_id, balance, last_update) 
            VALUES (1, 0, CURRENT_TIMESTAMP)
        """)

        cursor.execute("""
            INSERT OR IGNORE INTO user_balance (user_id, balance, last_update) 
            VALUES (2, 500, CURRENT_TIMESTAMP)
        """)

        cursor.execute("""
            INSERT OR IGNORE INTO user_balance (user_id, balance, last_update) 
            VALUES (3, 1000, CURRENT_TIMESTAMP)
        """)

        self.connection.commit()
        print("Atm.db has been created successfully")


    def close_connection_to_db(self):
        self.connection.close()


    def is_correct_credentials(self, username, password):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT * FROM users 
            WHERE username=? AND password=?
        """, (username, password))

        user = cursor.fetchone()

        if user is None:
            return False

        return True


    def is_user_admin(self, username):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT is_admin FROM users
            WHERE username=?
        """, (username,))

        result = cursor.fetchone()

        if result[0] == 1:
            return True

        return False


    def check_balance(self, username):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT balance 
            FROM user_balance AS us_b
            JOIN users AS u
            ON us_b.user_id=u.id
            WHERE username=?
        """, (username,))

        result = cursor.fetchone()

        if result is None:
            self.insert_initial_balance_sum(username, 0)
            balance = 0
            
        else:
            balance = result[0]

        return balance


    def insert_initial_balance_sum(self, username, initial_balance):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id 
            FROM users
            WHERE username=?
        """, (username,))

        user_id = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO user_balance (user_id, balance, last_update) 
            VALUES (?, ?, ?)
        """, (user_id, initial_balance, datetime.now()))

        self.connection.commit()


    def update_balance(self, username, new_balance):
        cursor = self.connection.cursor()

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

        self.connection.commit()


    def add_transaction(self, username, transaction_type, transaction_amount):
        cursor = self.connection.cursor()

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

        self.connection.commit()


    def check_atm_balance_sum(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT sum(nominal * count)
            FROM atm_balance
        """)

        result = cursor.fetchone()

        return result[0]


    def get_atm_balance(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT * 
            FROM atm_balance
        """)

        return cursor.fetchall()


    def change_atm_banknote_balance(self, nominal, banknote_amount):
        cursor = self.connection.cursor()

        cursor.execute("""
            UPDATE atm_balance
            SET count=?
            WHERE nominal=? 
        """, (banknote_amount, nominal))

        self.connection.commit()


    def user_exists(self, username):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT username 
            FROM users
            WHERE username=?
        """, (username,))

        result = cursor.fetchone()

        return result is not None and len(result) > 0


    def insert_new_user_to_db(self, username, password):
        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT INTO users (username, password, is_admin) 
            VALUES (?, ?, 0)
        """, (username, password))

        self.connection.commit()


ATM(DB_PATH).start()
