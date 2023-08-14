# ✔ Создайте класс прямоугольник.
# ✔ Класс должен принимать длину и ширину при создании
# экземпляра.
# ✔ У класса должно быть два метода, возвращающие периметр
# и площадь.
# ✔ Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# * doctest,
# * unittest,
# * -->pytest.


import pytest


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b


    def get_length(self):
        return 2 * (self.a + self.b)


    def get_area(self):
        return self.a * self.b


def test_get_length1():
    r1 = Rectangle(5, 7)
    assert(24 == Rectangle.get_length(r1))


def test_get_length2():
    r2 = Rectangle(3, 8)
    assert(22 == Rectangle.get_length(r2))


def test_get_length3():
    r3 = Rectangle(6)
    assert(20 == Rectangle.get_length(r3))


def test_get_area1():
    r4 = Rectangle(2, 4)
    assert(8 == Rectangle.get_area(r4))


def test_get_area2():
    r5 = Rectangle(9)
    assert(38 == Rectangle.get_area(r5))


if __name__ == '__main__':
    pytest.main()
