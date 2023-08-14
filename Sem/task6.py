# ✔ На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# ✔ Напишите 3-7 тестов pytest для данного проекта.
# ✔ Используйте фикстуры.


import sem13_6
import pytest
import json


@pytest.fixture
def new_data():
    data = {"1": ["John", 4],
            "2": ["Ben", 1],
            "5": ["Иван", 5],
            "4": ["Ольга", 5]}
    with open('test.json', 'w', encoding='UTF-8') as f1:
        json.dump(data, f1)
    return data


@pytest.fixture
def new_project(new_data):
    p = sem13_6.Project('test.json')
    p.enter(id='2', name='Ben')
    return p


@pytest.fixture
def new_user():
    return dict(id='7', name='Steve', level=2)


def test_add_user(new_user, new_project,new_data):
    # tmp = new_project.users.copy()
    # tmp.add(sem13_6.User(id=7, name='Steve', level=2))
    num_users=len(new_project.users)
    new_project.add_user(**new_user)

    # new_data['7'] = ['Steve', 2]
    assert (len (new_project.users) == num_users+1)


if __name__ == '__main__':
    pytest.main()
