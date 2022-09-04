class User:
    """Обычный пользователь"""

    def __init__(self, first_name, last_name, birth_date):
        """Инициализация атрибутов пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.login_attempts = 0

    def describe_user(self):
        """Выводит описание профиля юзера"""
        print(f"{self.first_name.title()} {self.last_name.title()} was born {self.birth_date}.")

    def greed_user(self):
        """Выводит приветствие"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Увеличивает кол-во попыток входа на 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет кол-во попыток входа"""
        self.login_attempts = 0


class Admin(User):
    """Представляет аспекты для админа"""

    def __init__(self, first_name, last_name, birth_date):
        """Инициализация атрибутов админа"""
        super().__init__(first_name, last_name, birth_date)
        self.admin_privileges = Privileges()


class Privileges:
    """Представляет особые привилегии пользователя"""

    def __init__(self):
        """Инициализация атрибутов привилегий"""
        self.privileges = ['allowed to add users', 'allowed to delete users', 'allowed to ban users']

    def show_privileges(self):
        """Выводит привилегии админа"""
        print(f"User privileges: {self.privileges}.")


user1 = User('Ivan', 'Ivanov', '20.04.78')
user1.describe_user()
user1.greed_user()
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

user2 = User('Alexandr', 'Alexandrov', '02.07.88')
user2.describe_user()
user2.greed_user()

admin1 = Admin('Vladimir', 'Vladimirov', '01.01.01')
admin1.describe_user()
admin1.greed_user()
admin1.admin_privileges.show_privileges()
