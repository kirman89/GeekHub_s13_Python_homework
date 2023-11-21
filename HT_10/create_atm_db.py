import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).parent
DB_PATH = Path(BASE_DIR, "atm.db")


def create_atm_db():
    connection = sqlite3.connect(DB_PATH)

    try:
        with connection:
            cursor = connection.cursor()

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

            cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
            cursor.executemany("INSERT INTO atm_balance VALUES (?,?)", bills)

            cursor.execute("""
                INSERT OR IGNORE INTO user_balance (user_id, balance) 
                VALUES (1, 0)
            """)

            cursor.execute("""
                INSERT OR IGNORE INTO user_balance (user_id, balance) 
                VALUES (2, 500)
            """)

            cursor.execute("""
                INSERT OR IGNORE INTO user_balance (user_id, balance) 
                VALUES (3, 1000)
            """)

            connection.commit()
            print("Atm.db has been created successfully")

    except Exception as e:
        print("Error while working with SQLite3", e)

    finally:
        if connection:
            connection.close()
            print("SQLite3 connection is closed")


create_atm_db()
