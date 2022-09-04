class Restaurant:
    """Обычный ресторан"""

    def __init__(self, restaurant_name, kitchen_type):
        """Инициализация атрибутов ресторана"""
        self.restaurant_name = restaurant_name
        self.kitchen_type = kitchen_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит описание ресторана"""
        r_name = f"Restaurant name is '{self.restaurant_name.title()}'."
        k_type = f"Kitchen is {self.kitchen_type.lower()}."
        print(r_name, k_type, sep="\n")

    def open_restaurant(self):
        """Выводит сообщение об открытии ресторана"""
        print(f"Restaurant '{self.restaurant_name.title()}' is open.")

    def read_number_served(self):
        """Выводит кол-во гостей ресторана"""
        print(f"Served {self.number_served} guests.")

    def set_number_served(self, served):
        """Изменяет кол-во гостей"""
        self.number_served = served

    def increment_number_served(self, i):
        """Увеличивает кол-во гостей на заданное число"""
        self.number_served += i


class IceCreamStand(Restaurant):
    """Представляет аспекты ресторана специфические для ресторана мороженого"""

    def __init__(self, restaurant_name, kitchen_type, *flavors):
        """Инициализация атрибутов ресторана мороженого"""
        super().__init__(restaurant_name, kitchen_type)
        self.flavors = flavors

    def read_flavors(self):
        """Выводит список сортов мороженого"""
        return print(f"List of flavors: {self.flavors}.")


restaurant1 = Restaurant("Sashka", "Russian")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(5)
restaurant1.read_number_served()

restaurant2 = Restaurant("aleks", "Georgian")
restaurant2.describe_restaurant()
restaurant2.increment_number_served(7)
restaurant2.read_number_served()

ice_cream_stand = IceCreamStand("Ice Cream", "International", 'Chocolate', 'Vanilla', 'Coconut')
ice_cream_stand.describe_restaurant()
ice_cream_stand.read_flavors()
