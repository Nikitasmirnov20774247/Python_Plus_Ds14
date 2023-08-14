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
# * -->doctest,
# * unittest,
# * pytest.


import doctest
from datetime import datetime as dt
from calendar import isleap


def check_year(current_date):
    '''
    >>> check_year("22.07.2020")
    True
    >>> check_year("14.8.2011")
    False
    >>> check_year("08.11.2023")
    True
    '''

    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    return (isleap(year))


def check_date(current_date):
    '''
    >>> check_date("22.07.2020")
    True
    >>> check_date("14.44.2011")
    False
    >>> check_date("08.33.2023")
    True
    '''

    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    try:
        dt(year=year, month=month, day=day)
    except:
        return False
    return True


if __name__ == '__main__':
    doctest.testmod(verbose=True)
