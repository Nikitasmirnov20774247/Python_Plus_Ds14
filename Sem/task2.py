# ✔ Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# * возврат строки без изменений
# * возврат строки с преобразованием регистра без потери
# символов
# * возврат строки с удалением знаков пунктуации
# * возврат строки с удалением букв других алфавитов
# * возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


from string import ascii_letters as as_lett
import doctest


def check_english(str1):
    """
    >>> check_english ('absdhisajfi')
    'absdhisajfi'
    >>> check_english ('aBsdHisaJfi')
    'absdhisajfi'
    >>> check_english ('ab,sdh!isaj?fi')
    'absdhisajfi'
    >>> check_english ('absЖdhшisajЩfi')
    'absdhisajfi'
    >>> check_english ('ab,Ж sdh!isaЫФАj? fi')
    'ab sdhisaj fi'

    """

    str2 = ''
    for i in str1:
        if i in as_lett or i == ' ':
            str2 += i
    return str2.lower()

if __name__ == '__main__':
    doctest.testmod(verbose=True)
