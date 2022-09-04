import math


class Pr:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def per(self):  # Периметр
        a = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        b = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        c = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        d = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        P = a + b + c + d
        return P

    def sq(self):  # Площадь
        a = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        b = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        S = a * b
        return S

    def __eq__(self, g):  # Проверка на равенство
        if self.sq() == g.sq():
            return True
        else:
            return False

    def perenos(self, vecx, vecy):
        self.x1 = self.x1 + vecx
        self.y1 = self.y1 + vecy
        self.x2 = self.x2 + vecx
        self.y2 = self.y2 + vecy
        self.x3 = self.x3 + vecx
        self.y3 = self.y3 + vecy
        self.x4 = self.x4 + vecx
        self.y4 = self.y4 + vecy
        return self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4

    def info(self):
        print("\nКоординаты: ", (self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4))
        print("Площадь: ", self.sq(), "\nПериметр: ", self.per())


pr1 = Pr(1, 1, 2, 1, 2, 0, 1, 0)
pr2 = Pr(1, 1, 3, 1, 3, 0, 1, 0)
print("Периметр = ", str(pr1.per()))
print("Площадь = ", str(pr1.sq()))
print("Периметр = ", str(pr2.per()))
print("Площадь = ", str(pr2.sq()))
print("Равны ли прямоугольники: ", pr1 == pr2)
pr1.info()
print("Парал. перенос: ", pr1.perenos(2, 3))
