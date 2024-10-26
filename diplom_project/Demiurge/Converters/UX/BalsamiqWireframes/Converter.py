import sqlite3
import json
import codecs
import chardet
import os


class Converter:
    '''
     description: Converter UX bmpr-to-json for code generator
     input: sqlite database as bmpr file by Balsamiq Wireframes
     output: json file ux formate
     developer: Roman Korolev
     contact: Orodunaar@mail.ru
    '''

    def __init__(self, path):
        self.db_path = path
        self.ui_format = {
            "branches": [],
            "resources": [],
            "comments": [],
            "users": [],
            "thumbnails": [],
            "info": {}
        }

    def decode_unicode_escape(self, text):
        """Преобразует кодировку 'unicode_escape' в формат 'utf-8'."""
        try:
            # Сначала проверяем, является ли текст строкой
            if isinstance(text, str):
                # Кодируем в байты
                byte_data = text.encode('utf-8')
                local_type = self.detect_encoding(byte_data)

                # Проверяем кодировку
                if local_type[0] == 'unicode_escape' and local_type[1] > 0.6:
                    # Декодируем с использованием unicode_escape
                    return codecs.decode(byte_data, 'unicode_escape')
                else:
                    return text
            else:
                # print(f"Ошибка декодирования: ожидается строка, но получен тип {type(text)}")
                return text
        except Exception as e:
            print(f"Ошибка декодирования: {e}")
            return text

    def detect_encoding(self, byte_data):
        """Определяет кодировку данных."""
        if isinstance(byte_data, bytes) or isinstance(byte_data, bytearray):
            result = chardet.detect(byte_data)
            return result['encoding'], result['confidence']
        else:
            print(f"Ошибка определения кодировки: ожидаются байты или bytearray, но получен тип {type(byte_data)}")
            return None, 0

    def convert_to_ui_format(self, data):
        # Конвертируем ветки
        for branch in data["branches"]:
            branch_attributes = json.loads(branch[1])  # предполагаем, что ATTRIBUTES в формате JSON
            branch_attributes["name"] = self.decode_unicode_escape(branch_attributes.get("name", ""))
            self.ui_format["branches"].append({
                "id": branch[0],
                "attributes": branch_attributes
            })

        # Конвертируем ресурсы
        for resource in data["resources"]:
            resource_attributes = json.loads(resource[2])
            resource_attributes["name"] = self.decode_unicode_escape(resource_attributes.get("name", ""))

            # Декодируем поле 'data', если оно есть
            resource_data = resource[3]
            if isinstance(resource_data, str):
                try:
                    resource_data = json.loads(resource_data)  # Пробуем разобрать JSON
                except json.JSONDecodeError as e:
                    print(f"Ошибка декодирования JSON: {e}")
                    resource_data = {}

                # Декодируем, если это строка
                resource_data = self.decode_unicode_escape(resource_data)

            self.ui_format["resources"].append({
                "id": resource[0],
                "branchId": resource[1],
                "attributes": resource_attributes,
                "data": resource_data
            })

        # Конвертируем комментарии
        for comment in data["comments"]:
            comment_attributes = json.loads(comment[5])
            comment_attributes["name"] = self.decode_unicode_escape(comment_attributes.get("name", ""))

            self.ui_format["comments"].append({

                "id": comment[0],
                "branchId": comment[1],
                "resourceId": comment[2],
                "data": self.decode_unicode_escape(comment[3]),  # Декодируем, если это строка
                "userId": comment[4],
                "attributes": comment_attributes
            })

            # Конвертируем пользователей
            for user in data["users"]:
                user_attributes = json.loads(user[1])
                user_attributes["name"] = self.decode_unicode_escape(user_attributes.get("name", ""))

                self.ui_format["users"].append({
                    "id": user[0],
                    "attributes": user_attributes
                })

            # Конвертируем миниатюры
            for thumbnail in data["thumbnails"]:
                thumbnail_attributes = json.loads(thumbnail[1])
                thumbnail_attributes["name"] = self.decode_unicode_escape(thumbnail_attributes.get("name", ""))

                self.ui_format["thumbnails"].append({
                    "id": thumbnail[0],
                    "attributes": thumbnail_attributes
                })

            # Конвертируем информацию
            for info in data["info"]:
                self.ui_format["info"][info[0]] = self.decode_unicode_escape(info[1])  # Декодируем, если это строка

            return self.ui_format

    def __adaptation(self):
        # Обработка данных
        for table_name, table_data in self.ui_format.items():
            print(f"Обработка таблицы: {table_name}")
            self.process_table(table_data)

    # def json_to_bmpr(self, input_file_path):
    #    self.__open(input_file_path)

    def bmpr_to_json(self, ui_output_file):
        # Получаем данные
        data = self.fetch_data_from_database()

        # Конвертируем данные
        self.convert_to_ui_format(data)

        self.__adaptation()

        self.__save(ui_output_file)

    def fetch_data_from_database(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # Считываем данные из всех таблиц
        branches = cursor.execute("SELECT * FROM BRANCHES").fetchall()
        resources = cursor.execute("SELECT * FROM RESOURCES").fetchall()
        comments = cursor.execute("SELECT * FROM COMMENTS").fetchall()
        users = cursor.execute("SELECT * FROM USERS").fetchall()
        thumbnails = cursor.execute("SELECT * FROM THUMBNAILS").fetchall()
        info = cursor.execute("SELECT * FROM INFO").fetchall()

        connection.close()

        return {
            "branches": branches,
            "resources": resources,
            "comments": comments,
            "users": users,
            "thumbnails": thumbnails,
            "info": info
        }

    def decode_unicode_string(self, s):
        try:
            return s.encode('latin1').decode('unicode_escape')
        except Exception as e:
            # print(f"Ошибка при декодировании строки: {s} - {e}")
            return s

    def process_table(self, table_data):
        for item in table_data:
            for key, value in item.items():
                if key in ['text', 'name']:
                    item[key] = self.decode_unicode_string(value)
                elif isinstance(value, dict):
                    self.process_table([value])
                elif isinstance(value, list):
                    self.process_table(value)

    def __open(self, input_file_path=""):
        # Чтение данных из файла
        with open(input_file_path, "r", encoding="utf-8") as f:
            self.ui_format = json.load(f)

    def __save(self, output_file_path=""):
        # Запись откорректированных данных в новый файл
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(self.ui_format, f, ensure_ascii=False, indent=2)
            print(f"Данные успешно записаны в {output_file_path}")

    def __create_database_if_not_exists(self, db_file):
        # Проверка на существование файла базы данных
        if not os.path.exists(db_file):
            print(f"Файл '{db_file}' не найден. Создаю новый файл базы данных...")
            # Подключение к базе данных (создание, если файл не существует)
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Создание таблицы BRANCHES
            cursor.execute('''CREATE TABLE IF NOT EXISTS BRANCHES (
                                ID VARCHAR(255) PRIMARY KEY, 
                                ATTRIBUTES TEXT)''')

            # Создание таблицы USERS
            cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (
                                ID VARCHAR(255) PRIMARY KEY, 
                                ATTRIBUTES TEXT)''')

            # Создание таблицы RESOURCES
            cursor.execute('''CREATE TABLE IF NOT EXISTS RESOURCES (
                                ID VARCHAR(255), 
                                BRANCHID VARCHAR(255), 
                                ATTRIBUTES TEXT, 
                                DATA LONGTEXT, 
                                PRIMARY KEY (ID, BRANCHID), 
                                FOREIGN KEY (BRANCHID) REFERENCES BRANCHES(ID))''')

            # Создание таблицы THUMBNAILS
            cursor.execute('''CREATE TABLE IF NOT EXISTS THUMBNAILS (
                                ID VARCHAR(255) PRIMARY KEY, 
                                ATTRIBUTES MEDIUMTEXT)''')

            # Создание таблицы INFO
            cursor.execute('''CREATE TABLE IF NOT EXISTS INFO (
                                NAME VARCHAR(255) PRIMARY KEY, 
                                VALUE TEXT)''')

            # Создание таблицы COMMENTS
            cursor.execute('''CREATE TABLE IF NOT EXISTS COMMENTS (
                                ID VARCHAR(255) PRIMARY KEY, 
                                BRANCHID VARCHAR(255), 
                                RESOURCEID VARCHAR(255), 
                                DATA LONGTEXT, 
                                USERID VARCHAR(255), 
                                ATTRIBUTES TEXT, 
                                FOREIGN KEY (USERID) REFERENCES USERS(ID), 
                                FOREIGN KEY (RESOURCEID, BRANCHID) REFERENCES RESOURCES(ID, BRANCHID))''')

            # Сохранение изменений и закрытие соединения
            conn.commit()
            conn.close()
            print(f"База данных '{db_file}' успешно создана.")
        else:
            print(f"Файл базы данных '{db_file}' уже существует.")

    def populate_database_from_json(self, json_file, db_file):
        # Проверка на существование базы данных и создание её, если не существует
        self.create_database_if_not_exists(db_file)

        # Открываем JSON файл и читаем его содержимое
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Подключаемся к базе данных SQLite
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Наполняем таблицу BRANCHES
        for branch in data.get('branches', []):
            self.insert_branch(cursor, branch)

        # Наполняем таблицу RESOURCES
        for resource in data.get('resources', []):
            self.insert_resource(cursor, resource)

        # Если есть другие данные (comments, users и т.д.), добавляем их
        # Сохранение изменений и закрытие соединения
        conn.commit()
        conn.close()

    def create_database_if_not_exists(self, db_file):
        if not os.path.exists(db_file):
            print(f"Файл '{db_file}' не найден. Создаю новый файл базы данных...")
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Создание структуры таблиц
            cursor.execute('''CREATE TABLE IF NOT EXISTS BRANCHES (
                                ID VARCHAR(255) PRIMARY KEY, 
                                ATTRIBUTES TEXT)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (
                                ID VARCHAR(255) PRIMARY KEY, 
                                ATTRIBUTES TEXT)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS RESOURCES (
                                ID VARCHAR(255), 
                                BRANCHID VARCHAR(255), 
                                ATTRIBUTES TEXT, 
                                DATA LONGTEXT, 
                                PRIMARY KEY (ID, BRANCHID), 
                                FOREIGN KEY (BRANCHID) REFERENCES BRANCHES(ID))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS THUMBNAILS (
                                ID VARCHAR(255) PRIMARY KEY, 
                                ATTRIBUTES MEDIUMTEXT)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS INFO (
                                NAME VARCHAR(255) PRIMARY KEY, 
                                VALUE TEXT)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS COMMENTS (
                                ID VARCHAR(255) PRIMARY KEY, 
                                BRANCHID VARCHAR(255), 
                                RESOURCEID VARCHAR(255), 
                                DATA LONGTEXT, 
                                USERID VARCHAR(255), 
                                ATTRIBUTES TEXT, 
                                FOREIGN KEY (USERID) REFERENCES USERS(ID), 
                                FOREIGN KEY (RESOURCEID, BRANCHID) REFERENCES RESOURCES(ID, BRANCHID))''')

            conn.commit()
            conn.close()
            print(f"База данных '{db_file}' успешно создана.")
        else:
            print(f"Файл базы данных '{db_file}' уже существует.")

    def insert_branch(self, cursor, branch):
        attributes_json = json.dumps(branch.get('attributes', {}))
        cursor.execute('''
            INSERT INTO BRANCHES (ID, ATTRIBUTES)
            VALUES (?, ?)
        ''', (branch.get('id'), attributes_json))

    def insert_resource(self, cursor, resource):
        attributes_json = json.dumps(resource.get('attributes', {}))
        data_json = json.dumps(resource.get('data', {}))
        cursor.execute('''
            INSERT INTO RESOURCES (ID, BRANCHID, ATTRIBUTES, DATA)
            VALUES (?, ?, ?, ?)
        ''', (resource.get('id'), resource.get('branchId'), attributes_json, data_json))

    def json_to_bmpr(self, json_file):
        # Чтение данных из JSON файла
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Создание базы данных, если она не существует
        self.create_database_if_not_exists(self.db_path)

        # Подключаемся к базе данных
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Наполнение базовых таблиц данными
        self.insert_branches(cursor, data.get("branches", []))
        self.insert_resources(cursor, data.get("resources", []))
        self.insert_comments(cursor, data.get("comments", []))
        self.insert_users(cursor, data.get("users", []))
        self.insert_thumbnails(cursor, data.get("thumbnails", []))
        self.insert_info(cursor, data.get("info", {}))

        # Сохраняем изменения
        conn.commit()
        conn.close()

    def insert_branches(self, cursor, branches):
        for branch in branches:
            attributes = json.dumps(branch["attributes"], ensure_ascii=False)  # Конвертация атрибутов в JSON
            cursor.execute('''
                INSERT INTO BRANCHES (ID, ATTRIBUTES)
                VALUES (?, ?)
                ON CONFLICT(ID) DO UPDATE SET ATTRIBUTES=excluded.ATTRIBUTES
            ''', (branch["id"], attributes))

    def insert_resources(self, cursor, resources):
        for resource in resources:
            attributes = json.dumps(resource["attributes"], ensure_ascii=False)  # Конвертация атрибутов в JSON
            data = json.dumps(resource["data"], ensure_ascii=False)  # Конвертация данных в JSON
            cursor.execute('''
                INSERT INTO RESOURCES (ID, BRANCHID, ATTRIBUTES, DATA)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(ID, BRANCHID) DO UPDATE SET ATTRIBUTES=excluded.ATTRIBUTES, DATA=excluded.DATA
            ''', (resource["id"], resource["branchId"], attributes, data))

    def insert_comments(self, cursor, comments):
        for comment in comments:
            attributes = json.dumps(comment["attributes"], ensure_ascii=False)  # Конвертация атрибутов в JSON
            data = comment.get("data", "")
            cursor.execute('''
                INSERT INTO COMMENTS (ID, BRANCHID, RESOURCEID, DATA, USERID, ATTRIBUTES)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(ID) DO UPDATE SET DATA=excluded.DATA, ATTRIBUTES=excluded.ATTRIBUTES
            ''', (comment["id"], comment["branchId"], comment["resourceId"], data, comment["userId"], attributes))

    def insert_users(self, cursor, users):
        for user in users:
            attributes = json.dumps(user["attributes"], ensure_ascii=False)  # Конвертация атрибутов в JSON
            cursor.execute('''
                INSERT INTO USERS (ID, ATTRIBUTES)
                VALUES (?, ?)
                ON CONFLICT(ID) DO UPDATE SET ATTRIBUTES=excluded.ATTRIBUTES
            ''', (user["id"], attributes))

    def insert_thumbnails(self, cursor, thumbnails):
        for thumbnail in thumbnails:
            attributes = json.dumps(thumbnail["attributes"], ensure_ascii=False)  # Конвертация атрибутов в JSON
            cursor.execute('''
                INSERT INTO THUMBNAILS (ID, ATTRIBUTES)
                VALUES (?, ?)
                ON CONFLICT(ID) DO UPDATE SET ATTRIBUTES=excluded.ATTRIBUTES
            ''', (thumbnail["id"], attributes))

    def insert_info(self, cursor, info):
        for key, value in info.items():
            cursor.execute('''
                INSERT INTO INFO (NAME, VALUE)
                VALUES (?, ?)
                ON CONFLICT(NAME) DO UPDATE SET VALUE=excluded.VALUE
            ''', (key, value))


class UXElement:
    def __init__(self, properties):
        self.properties = properties

    def __repr__(self):
        return f"UXElement(properties={self.properties})"


# Пример использования
if __name__ == "__main__":
    db_path = "Collection component.bmpr"  # Укажите путь к вашей базе данных
    converter = Converter(db_path)
    converter.bmpr_to_json("Collection_component.json")
    # Пример использования:
    # populator = DatabasePopulator('database.bmpr')
    converter.json_to_bmpr('Collection_component.json')
