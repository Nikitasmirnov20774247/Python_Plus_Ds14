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
# * -->doctest,
# * unittest,
# * pytest.

import doctest


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b


    def get_length(self):
        """
        >>> r1 = Rectangle(5, 7)
        >>> Rectangle.get_length (r1)
        24
        >>> r2 = Rectangle(3, 8)
        >>> Rectangle.get_length (r2)
        22
        >>> r3 = Rectangle(6)
        >>> Rectangle.get_length (r3)
        20
        """
        return 2 * (self.a + self.b)


    def get_area(self):
        """
        >>> r4 = Rectangle(2, 4)
        >>> Rectangle.get_area(r4)
        8
        >>> r5 = Rectangle(9)
        >>> Rectangle.get_area(r5)
        38
        """
        return self.a * self.b


if __name__ == '__main__':
    doctest.testmod(verbose=True)
