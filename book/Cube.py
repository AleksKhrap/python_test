from random import randint


class Cube:
    """Бросание кубика"""

    def __init__(self, sides=6):
        """Инициализация атрибутов куба"""
        self.sides = sides

    def roll_cube(self):
        """Выводит случайное число"""
        print(randint(1, self.sides))


cube1 = Cube()
cube1.roll_cube()
cube1.roll_cube()
cube1.roll_cube()

print('\n')

cube2 = Cube(10)
cube2.roll_cube()
cube2.roll_cube()
cube2.roll_cube()

print('\n')

cube3 = Cube(20)
cube3.roll_cube()
cube3.roll_cube()
cube3.roll_cube()