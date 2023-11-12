""" 3. Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль
      (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс 
      (файл <{username}_balance.TXT>) та 
      історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова
      перевірка введених даних (введено цифри; знімається не більше,
      ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу 
      (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка 
      додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете 
      реалізувати ф-л додавання нового користувача - не стримуйтесь :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow
      банкомата:
      - на початку роботи - логін користувача (програма запитує 
      ім'я/пароль). Якщо вони неправильні - вивести повідомлення про 
      це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже 
      закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, 
      але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, 
    json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
"""


import csv
import json


def login():
   max_attempts = 3
   current_attempt = 0

   while current_attempt < max_attempts:
      username = input("Enter username: ")
      password = input("Enter password: ")

      if is_valid_credentials(username, password):
         print(f"\nWelcome, {username}!")
         return username

      else:
         print("Credentials are not valid. Try again.")
         current_attempt += 1

   print("You have reached the limit of attempts. Goodbye!")
   exit()


def is_valid_credentials(username, password):

   with open('users.csv') as file:
      text = csv.reader(file)

      for row in text:
         if row[0] == username and row[1] == password:

            return True

   return False


def check_balance(username):
   balance_filename = username + '_balance.txt'

   try:
      with open(balance_filename, 'r') as file:
         balance = int(file.read())
      return balance

   except ValueError:
      return 0


def display_balance(balance):
   print(f"\nCurrent balance: {balance} UAH")


def update_balance(username, new_balance):
   balance_filename = username + '_balance.txt'

   with open(balance_filename, 'w') as balance_file:
      balance_file.write(str(new_balance))


def read_exist_transactions(username):
   transaction_filename = username + '_transactions.json'
   try:
      with open(transaction_filename, 'r') as transaction_file:
         return json.load(transaction_file)

   except json.JSONDecodeError:
        return []


def add_transaction(username, transaction_type, transaction_amount):
   transaction_filename = username + '_transactions.json'
   exist_transactions = read_exist_transactions(username)

   transaction = [{
      'transaction_type': transaction_type,
      'transaction_amount': transaction_amount
   }]
   transaction_list = exist_transactions + transaction

   with open(transaction_filename, 'w') as transaction_file:
      json.dump(transaction_list, transaction_file)


def is_positive_amount(amount):
   return amount > 0


def deposit_money(username):

   balance = check_balance(username)
   try:
      amount = int(input("\nEnter the amount you want to deposit: "))
   
   except ValueError:
      print("You entered invalid amount!")
      return

   else:
      if not is_positive_amount(amount):
         print("Amount must be positive!")
         return

      balance += amount
      update_balance(username, balance)
      add_transaction(username, 'deposit_money', amount)

      print(f"\nBalance was replenished by {amount} UAH.")
      display_balance(balance)


def withdraw_money(username):

   balance = check_balance(username)
   try:
      amount = int(input("\nEnter the amount you want to withdraw: "))

   except ValueError:
      print("You entered invalid amount!")
      return

   else:
      if not is_positive_amount(amount):
         print("Amount must be positive!")
         return

      if amount > balance:
         print("Insufficient funds to withdraw. Try a smaller amount.")
         return

      balance -= amount
      update_balance(username, balance)
      add_transaction(username, 'withdraw_money', amount)

      print(f"\nThe {amount} UAH was withdrawn from the balance.")
      display_balance(balance)


def display_menu():
   print("\n\nMenu:\n1. Check balance\n2. Deposit money")
   print("3. Withdraw money\n4. End session")


def end_session(username):
   print(f"\n{username}, have a nice day!")
   exit()


def start():
   username = login()

   while True:
      display_menu()
      user_choice = input(f"{'-'*10}\nChoose an action (1-4): ")

      if user_choice == '1':
         display_balance(check_balance(username))

      elif user_choice == '2':
         deposit_money(username)

      elif user_choice == '3':
         withdraw_money(username)

      elif user_choice == '4':
         end_session(username)

      else:
         print("Incorrect input. Try again.")


start()
