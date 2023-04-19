import sqlite3 as sq
import asyncio


class User:
    @classmethod
    def add_plus_operation(cls, name):
        """
        Added operation-info into dataframe.
        :param name:
        :return: None
        """
        with sq.connect('kwargs/operation.db') as db:
            cur = db.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS operation (
                    user_id INTEGER,
                    transaction_amount INTEGER,
                    date DATE,
                    category TEXT
                    )""")

            s = input("Enter space-separated transaction amount, date, category: ").split()

            cur.execute(
                f"""INSERT INTO operation (user_id, transaction_amount, date, category) VALUES {cls.get_user_id(name), *s}""")

            print("Added.")

    @classmethod
    def add_minus_operation(cls, name):
        with sq.connect('kwargs/operation.db') as db:
            cur = db.cursor()

            def date_to_sql(date):
                if date == "":
                    return ""
                return f" AND \"{date[0:10]}\" <= DATE <= \"{date[11:-1]}\"" if "-" in date else f" AND DATE == \"{date}\""

            def category_to_sql(category):
                return "" if category == "" else f" AND category == {category}"

            def transaction_amount_to_sql(transaction_amount):
                return "" if transaction_amount == "" else f" AND transaction_amount == {transaction_amount}"

            transaction_amount = input("Specify transaction amount, if know, else press Enter: ")

            date = date_to_sql(
                input("Specify the date or date-interval(format: dd.mm.ee-dd.mm.ee, if know, else press Enter: "))

            category = category_to_sql(input("Specify the transaction, if know, else press Enter: "))

            cur.execute(
                f"""DELETE FROM operation WHERE user_id == {cls.get_user_id(name)}{transaction_amount}{date}{category}""")

            print("Removed.")

    @classmethod
    def show_operation(cls, name):
        with sq.connect('kwargs/operation.db') as db:
            cur = db.cursor()

            def date_to_sql(date):
                if date == "":
                    return ""
                return f" AND \"{date[0:10]}\" <= DATE <= \"{date[11:-1]}\"" if "-" in date else f" AND DATE == \"{date}\""

            def category_to_sql(category):
                return "" if category == "" else f" AND category == {category}"

            def transaction_amount_to_sql(transaction_amount):
                return "" if transaction_amount == "" else f" AND transaction_amount == {transaction_amount}"

            transaction_amount = input("Specify transaction amount, if know, else press Enter: ")

            date = date_to_sql(
                input("Specify the date or date-interval(format: dd.mm.ee-dd.mm.ee, if know, else press Enter: "))

            category = category_to_sql(input("Specify the transaction, if know, else press Enter: "))

            cur.execute(
                f"""SELECT transaction_amount, date, category FROM operation
                WHERE user_id == {cls.get_user_id(name)}{transaction_amount}{date}{category}""")

            for i in cur.fetchall():
                print(*i)

    def exit(name):
        print("\n----------", "\nHave a good day!")

    def get_user_id(name):
        with sq.connect('kwargs/users.db') as db:
            cur = db.cursor()

            cur.execute(F"""SELECT user_id FROM users
            WHERE name == \"{name}\"""")

            return cur.fetchone()[0]

    @classmethod
    def greetings(self) -> str:
        """
        Method for greetings new and exist's users.
        :return: name_user
        """
        with sq.connect('kwargs/users.db') as db:
            cur = db.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )""")

            name_user = input('Hello! Please, enter your name: ')

            cur.execute("""SELECT name FROM users""")

            flag = False
            for i in cur:
                if name_user in i:
                    print(f"We're glad to have you back, {name_user}.")
                    flag = True
                    break
            if not flag:
                print(f"Nice to meet you, {name_user}.")
                cur.execute(f"""INSERT INTO users (name) VALUES ("{name_user}")""")
            return name_user

    @classmethod
    def select_actions(self):
        print("\n----------", "\nChoose category:")
        print("""1 - add operation
2 - remove operation
3 - show operation
0 - exit""")
        return input("Inputn category number: ")
