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
# * -->unittest,
# * pytest.


import unittest


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b


    def get_length(self):

        return 2 * (self.a + self.b)


    def get_area(self):

        return self.a * self.b


class TestCheckRectangle(unittest.TestCase):
    def test_get_length1(self):
        r1 = Rectangle(5, 7)
        self.assertEqual(24, Rectangle.get_length(r1))


    def test_get_length2(self):
        r2 = Rectangle(3, 8)
        self.assertEqual(22, Rectangle.get_length(r2))


    def test_get_length3(self):
        r3 = Rectangle(6)
        self.assertEqual(20, Rectangle.get_length(r3))


    def test_get_area1(self):
        r4 = Rectangle(2, 4)
        self.assertEqual(8, Rectangle.get_area(r4))


    def test_get_area2(self):
        r5 = Rectangle(9)
        self.assertEqual(38, Rectangle.get_area(r5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
