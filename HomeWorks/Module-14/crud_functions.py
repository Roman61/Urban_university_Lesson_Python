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
