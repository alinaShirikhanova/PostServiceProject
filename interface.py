import datetime
from tkinter import *
from tkinter import ttk


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
        if value < 0:
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

    def __init__(self, user_id: int, login: str, password: str, name: str, surname: str, phone: str, email: str,
                 birthdate: str, status: int):
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


class Window(Tk):
    def __init__(self, add_user_func, load_users_func, get_statuses_dict_func):
        super().__init__()
        self.title('Post Service')
        self.geometry('+300+100')

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)
        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text='Просмотр пользователей')

        frame2 = ttk.Frame()
        frame2.pack()
        notebook.add(frame2, text='Добавление пользователя')

        columns = ['id', 'login', 'password', 'name', 'surname', 'phone', 'email', 'berthdate', 'status']
        self.users_table = ttk.Treeview(columns=columns, show='headings', master=frame1)

        columns_names = ['ID', 'Login', 'Password', 'Name', 'Surname', 'Phone', 'Email', 'Birthdate', 'Status']
        columns_width = [30, 100, 100, 120, 120, 150, 150, 100, 100]

        for i in range(len(columns)):
            self.users_table.heading(columns[i], text=columns_names[i])
            self.users_table.column(f'#{i}', stretch=NO, width=columns_width[i])



        self.add_user_api_func = add_user_func
        self.load_users_api_func = load_users_func
        self.get_statuses_api_func = get_statuses_dict_func

        self.add_user_label = Label(text='Добавление пользователя', master=frame2)
        self.add_user_label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        self.login_label = Label(text='Логин*:', master=frame2)
        self.login_label.grid(row=1, column=0, padx=3, pady=3)
        self.login_input = ttk.Entry(master=frame2)
        self.login_input.grid(row=1, column=1, padx=3, pady=3)
        self.login_error = Label(master=frame2)
        self.login_error.grid(row=1, column=2, padx=3, pady=3)

        self.login_label = Label(text="Логин*:", master=frame2)
        self.login_label.grid(row=1, column=0, padx=3, pady=3)
        self.login_input = ttk.Entry(master=frame2)
        self.login_input.grid(row=1, column=1, padx=3, pady=3)
        self.login_error = Label(master=frame2)
        self.login_error.grid(row=1, column=2, padx=3, pady=3)

        self.password_label = Label(text="Пароль*:", master=frame2)
        self.password_label.grid(row=2, column=0, padx=3, pady=3)
        self.password_input = ttk.Entry(master=frame2)
        self.password_input.grid(row=2, column=1, padx=3, pady=3)
        self.password_error = Label(master=frame2)
        self.password_error.grid(row=2, column=2, padx=3, pady=3)

        self.name_label = Label(text="Имя*:", master=frame2)
        self.name_label.grid(row=3, column=0, padx=3, pady=3)
        self.name_input = ttk.Entry(master=frame2)
        self.name_input.grid(row=3, column=1, padx=3, pady=3)
        self.name_error = Label(master=frame2)
        self.name_error.grid(row=3, column=2, padx=3, pady=3)

        self.surname_label = Label(text="Фамилия*:", master=frame2)
        self.surname_label.grid(row=4, column=0, padx=3, pady=3)
        self.surname_input = ttk.Entry(master=frame2)
        self.surname_input.grid(row=4, column=1, padx=3, pady=3)
        self.surname_error = Label(master=frame2)
        self.surname_error.grid(row=4, column=2, padx=3, pady=3)

        self.phone_label = Label(text="Телефон:", master=frame2)
        self.phone_label.grid(row=5, column=0, padx=3, pady=3)
        self.phone_input = ttk.Entry(master=frame2)
        self.phone_input.grid(row=5, column=1, padx=3, pady=3)
        self.phone_error = Label(master=frame2)
        self.phone_error.grid(row=5, column=2, padx=3, pady=3)

        self.email_label = Label(text="Почта:", master=frame2)
        self.email_label.grid(row=6, column=0, padx=3, pady=3)
        self.email_input = ttk.Entry(master=frame2)
        self.email_input.grid(row=6, column=1, padx=3, pady=3)
        self.email_error = Label(master=frame2)
        self.email_error.grid(row=6, column=2, padx=3, pady=3)

        self.birthdate_label = Label(text="Дата рождения:", master=frame2)
        self.birthdate_label.grid(row=7, column=0, padx=3, pady=3)
        self.birthdate_input = ttk.Entry(master=frame2)
        self.birthdate_input.grid(row=7, column=1, padx=3, pady=3)
        self.birthdate_error = Label(master=frame2)
        self.birthdate_error.grid(row=7, column=2, padx=3, pady=3)

        self.status_label = Label(text="Статус*:", master=frame2)
        self.status_label.grid(row=8, column=0, padx=3, pady=3)
        self.statuses_list = list(self.get_statuses_api_func().keys())
        self.status_combobox = ttk.Combobox(values=self.statuses_list, master=frame2)
        self.status_combobox.grid(row=8, column=1, padx=3, pady=3)
        self.status_error = Label(master=frame2)
        self.status_error.grid(row=8, column=2, padx=3, pady=3)

        self.add_user_button = ttk.Button(text='Добавить пользователя', command=self.add_user, master=frame2)
        self.add_user_button.grid(row=9, column=1, padx=3, pady=3)

        self.users_list_variable = Variable()
        self.users_listbox = Listbox(listvariable=self.users_list_variable, master=frame1)
        self.users_listbox.grid(row=10, column=0, columnspan=3, padx=3, pady=3)

        self.load_users_button = ttk.Button(text='Обновить', command=self.load_users_list, master=frame1)
        self.load_users_button.grid(row=11, column=1, padx=3, pady=3)

        self.mainloop()

    def add_user(self):
        login = self.login_input.get()
        password = self.password_input.get()
        print(password)
        name = self.name_input.get()
        surname = self.surname_input.get()
        phone = self.phone_input.get() if self.phone_input.get() != '' else None
        email = self.email_input.get() if self.email_input.get() != '' else None
        birthdate = self.birthdate_input.get() if self.birthdate_input.get() != '' else None
        status = self.get_statuses_api_func().get(self.status_combobox.get())
        user = User(0, login, password, name, surname, phone, email, birthdate, status)
        self.add_user_api_func(user)

    def load_users_list(self):
        users = self.load_users_api_func()
        users_list = []
        for user in users:
            users_list.append(f'{user.id}. {user.login}, {user.password}, {user.name},'
                              f' {user.surname}, {user.phone}, {user.email}, {user.birthdate}, {user.status}')

        self.users_list_variable.set(users_list)
