import datetime
import sqlite3
import json
import traceback

db_filename = 'post_service.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   login TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL,
   name TEXT NOT NULL,
   surname TEXT NOT NULL,
   phone TEXT UNIQUE,
   email TEXT UNIQUE,
   birthdate DATE);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS addresses(
   addressid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   country TEXT,
   city TEXT,
   street TEXT,
   house TEXT,
   flat TEXT,
   postindex INTEGER NOT NULL,
   commentary TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   info TEXT NOT NULL,
   description TEXT,
   senderid INTEGER NOT NULL,
   courierid INTEGER NOT NULL,
   addressid INTEGER NOT NULL);
""")

# cur.execute("""ALTER TABLE users ADD COLUMN status INTEGER""")
# cur.execute("""ALTER TABLE orders ADD COLUMN status INTEGER""")

# создание таблица статусов заказов
cur.execute("""CREATE TABLE IF NOT EXISTS orderstatuses(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   status TEXT NOT NULL UNIQUE);
""")

# создание таблица статусов пользователей
cur.execute("""CREATE TABLE IF NOT EXISTS userstatuses(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   status TEXT NOT NULL UNIQUE);
""")


# заполнение таблицы
# cur.execute(f"""INSERT INTO userstatuses (status) VALUES ('administrator');""")
# cur.execute(f"""INSERT INTO userstatuses (status) VALUES ('courier');""")
# cur.execute(f"""INSERT INTO userstatuses (status) VALUES ('user');""")
# cur.execute(f"""INSERT INTO users (login, password, name, surname, status)
#   VALUES ('user', 'user', 'noname', 'noname', {3});""")
# cur.execute(f"""INSERT INTO users (login, password, name, surname, email, birthdate, status)
#   VALUES ('admin4563', '457297301', 'Иван', 'Петров', 'ivanpetrov@mail.ru', '1995-5-12', {1});""")
# cur.execute(f"""INSERT INTO users (login, password, name, surname, phone, birthdate, status)
#   VALUES ('vasiliyliyliy', 'orlov1990', 'Василий', 'Орлов', '+79993452845', '1990-10-24', {2});""")
# conn.commit()

# class Properties:
#     database_filename = ''
#
#     def __init__(self, input=dict()):
#         self.database_filename = input.get("database_filename")


# properties = Properties()
# properties.database_filename = "post_service.db"
# with open('properties.json', 'r') as openfile:
#     properties = json.load(openfile, object_hook=Properties)
# # print(properties.__dict__)
# # json_object = json.dumps(properties.__dict__)
# # with open('properties.json', 'w') as outfile:
# #     outfile.write(json_object)
#
#
#
# # Создать любой класс с 3 свойствами.
# # Записать свойства с их значениями в файл в формате json

class User:
    _id = 0
    _login = ''
    _password = ''
    _name = ''
    _surname = ''
    _phone = None
    _email = None
    _birthdate = None
    _status = 3

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise ValueError()
        self._id = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        if type(value) != str:
            raise TypeError()
        if len(value) < 8:
            raise TypeError()
        VALID_SYMBOLS = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`'
        for i in value:
            if i not in VALID_SYMBOLS:
                raise TypeError()
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError()
        if len(value) < 8:
            raise TypeError()
        VALID_SYMBOLS = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`'
        for i in value:
            if i not in VALID_SYMBOLS:
                raise TypeError()
        self._login = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) != str:
            raise TypeError()
        if len(value) == 0:
            raise TypeError()
        check = [True, True]
        letters_eng = 'abcdefghijklmnopqrstuvwxyz'
        letters_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
        for i in value:
            if i not in letters_eng:
                check[0] = False
        for i in value:
            if i not in letters_ru:
                check[0] = False
        if not check[0] and not check[1]:
            raise TypeError()
        if value[0].islower():
            raise TypeError()
        self._name = value

    @property
    def surname(self):
        return self._name

    @surname.setter
    def surname(self, value: str):
        if type(value) != str:
            raise TypeError()
        if len(value) == 0:
            raise TypeError()
        check = [True, True]
        letters_eng = 'abcdefghijklmnopqrstuvwxyz'
        letters_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
        for i in value:
            if i not in letters_eng:
                check[0] = False
        for i in value:
            if i not in letters_ru:
                check[0] = False
        if not check[0] and not check[1]:
            raise TypeError()
        if value[0].islower():
            raise TypeError()
        self._surname = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if value is None:
            self._phone = None
            return
        if type(value) != str:
            raise TypeError()
        if len(value) < 11:
            raise TypeError()
        if value[0] == '8':
            if not value.isnumeric() or not len(value) == 11:
                raise TypeError()
        elif value[0] == '+':
            if not value[1:].isnumeric():
                raise TypeError()
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if value is None:
            self._email = None
            return
        VALID_SYMBOLS = "abcdefghijklmnopqrstuvwxyz@_.0123456789"
        if type(value) != str:
            raise TypeError()
        if len(value) < 5:
            raise ValueError("длина почты слишком мала")
        if value.find(".", -4, -2) == -1:
            raise ValueError("некорректный домен")
        if value.find("@", 1) == -1:
            raise ValueError("собака не найдена")
        for i in value:
            if i not in VALID_SYMBOLS:
                raise ValueError("недопустимые символы")
        self._email = value

    def __repr__(self):
        return f'{self._id}. {self._name} {self._surname}'

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value: str):
        if value is None:
            self._birthdate = None
            return
        if type(value) != str:
            raise TypeError()
        nums = list(map(int, value.split('-')))
        date = datetime.date(nums[0], nums[1], nums[2])
        if date > datetime.date.today():
            raise ValueError()
        self._birthdate = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: int):
        if type(value) != int:
            raise TypeError()
        if value < 0:
            raise ValueError()
        self._status = value

    def __init__(self, user_id: int, login: str, password: str, name: str, surname: str, phone: str, email: str,  birthdate: str, status: int):
        self.id = user_id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.birthdate = birthdate
        self.status = status

# Точка должна быть либо -3, либо -4 символом
# @ начинается с первого символа
# Определить минимальную длину
# Проверка на тип

class Address:
    _id = 0
    _country = ''
    _city = ''
    _street = ''
    _house = ''
    _flat = ''
    _post_index = ''
    _commentary = ''


class Order:
    _id = 0
    _info = ''
    _description = ''
    _sender_id = 0
    _courier_id = 0
    _address_id = 0
    _status = 1


def get_all_users():
    cur.execute("""SELECT * FROM users""")
    rows = cur.fetchall()
    users = []
    for row in rows:

        user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        users.append(user)
    return users


print(get_all_users())


