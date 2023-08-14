# ✔ Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате
# DD.MM.YYYY
# ✔ Функция возвращает истину, если дата может
# существовать или ложь, если такая дата
# невозможна.
# ✔ Проверку года на високосность вынести в отдельную
# защищённую функцию.

# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# * doctest,
# * -->unittest,
# * pytest.


import unittest
from datetime import datetime as dt
from calendar import isleap


def check_year(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    return (isleap(year))


def check_date(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    try:
        dt(year=year, month=month, day=day)
    except:
        return False
    return True


class TestCheckDate(unittest.TestCase):
    def test_year1(self):
        self.assertEqual(True, check_year("22.07.2020"))


    def test_year2(self):
        self.assertEqual(False, check_year("14.8.2011"))


    def test_year3(self):
        self.assertEqual(True, check_year("08.11.2023"))


    def test_date1(self):
        self.assertEqual(True, check_date("22.07.2020"))


    def test_date2(self):
        self.assertEqual(False, check_date("14.44.2011"))


    def test_date3(self):
        self.assertEqual(True, check_date("08.33.2023"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
