class Car:
    """Простая модель авто"""

    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает данные об автомобиле"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данны одометра"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Обновляет данные одометра"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает кол-во миль на одометре"""
        self.odometer_reading += miles


class Battery:
    """Аккумуляторы"""

    def __init__(self, battery_size=75):
        """Инициализация атрибутов аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Увеличивает объем батареи"""
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Представляет аспекты машины специфические для электроавтомобиля"""

    def __init__(self, make, model, year):
        """Инициализация атрибутов электромобиля"""
        super().__init__(make, model, year)
        self.battery = Battery()


tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()

audi = Car('audi', 'a4', 2022)
print(audi.get_descriptive_name())
