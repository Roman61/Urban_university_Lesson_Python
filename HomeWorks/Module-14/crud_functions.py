import sqlite3
import random

dietary_supplements = {
    'Здоровые суставы': ['files/1.jpg', '1400 ₽', 'Гель Болотова "Здоровые суставы", ТМ "Центр Болотова" 100 мл.'],
    'От варикоза': ['files/2.jpg', '1400 ₽', 'Гель Болотова от варикоза, ТМ "Центр Болотова"'],
    'AQUA VITAE': ['files/3.jpg', '1100 ₽', 'Концентрат Серебра AQUA VITAE'],
    'Orzax Milk': ['files/4.jpg', '2100 ₽', 'ОРЗАКС МОЛОЧНЫЙ РАСПОРОПШИ ПЛЮС'],
}


class Engine:

    def __init__(self, db_name):
        self.name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self  # привязка к активному объекту with-блока

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.connection.commit()
            self.connection.close()
        except AttributeError:  # у объекта нет метода close
            print('Not closable.')
            return True  # исключение перехвачено

    def create_table_db(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                price INTEGER,
                img TEXT NOT NULL
                )
                ''')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER,
                growth INTEGER, 
                weight INTEGER
                )
                ''')

    def add_user(self, username, email, age, growth, weight):
        check_user = self.cursor.execute("SELECT * FROM Users WHERE username=?", (username,))

        if check_user.fetchone() is None:
            user_id = len(self.get_all_users()) + 1
            print(f'''
            INSERT INTO Users VALUES ('{user_id}','{username}','{email}', {age}, {growth}, {weight})
            ''')
            self.cursor.execute(f'''
            INSERT INTO Users VALUES ('{user_id}','{username}','{email}', {age}, {growth}, {weight})
            ''')
            self.connection.commit()

    def show_stat(self):
        count_users = self.cursor.execute("SELECT COUNT(*) FROM Users").fetchone()
        self.connection.commit()
        return count_users[0]

    def show_users(self):
        users_list = self.cursor.execute("SELECT * FROM Users").fetchall()
        message = ''
        for user in users_list:
            message += f'{user[0]} @{user[1]} {user[2]} {user[3]} {user[4]} {user[2]} \n'
        self.connection.commit()
        return message

    def check_user(self, username):
        check_user = self.cursor.execute("SELECT * FROM Users WHERE username=?", (username,))

        if check_user.fetchone() is None:
            return False
        else:
            return True

    def get_all_users(self):
        return self.cursor.execute('SELECT * FROM Users').fetchall()

    def add_product(self, product_id: int, title: str, description: str, price: int, img: str):
        check_product = self.cursor.execute('SELECT * FROM Products WHERE id=?', (product_id,))

        if check_product.fetchone() is None:
            self.cursor.execute(f'''
                INSERT INTO Products VALUES('{product_id}', '{title}', '{description}', '{price}', '{img}')
            ''')
            self.connection.commit()

    def initiate_db(self):
        self.create_table_db()
        for k, v in enumerate(dietary_supplements):
            self.add_product(k, v, dietary_supplements[v][2], dietary_supplements[v][1], dietary_supplements[v][0])

    def drop_table_products(self):
        self.cursor.execute("DROP TABLE IF EXISTS Products")

    def get_all_products(self):
        return self.cursor.execute('SELECT * FROM Products').fetchall()
