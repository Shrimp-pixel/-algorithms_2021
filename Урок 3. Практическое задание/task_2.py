"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

from hashlib import sha256
from random import randint


def hashpassword(login, password):
    hashpw = sha256(login.encode() + password.encode()).hexdigest()
    return hashpw


def createDB():
    with open("DB.csv", 'w') as f:
        with open("users_password(not_hashed).csv", 'w') as p:
            for i in range(10):
                password = str(randint(1000, 10000))
                #print(password)
                p.writelines("login" + str(i) + "," + password + '\n')
                f.writelines("login" + str(i) + "," + str(hashpassword("login" + str(i), password)) + "\n")


def validation(login):
    password = input("Введите пароль еще раз для проверки:")
    with open("DB.csv", 'r') as f:
        for line in f:
            log_password = line[:-1].split(',')
            if log_password[0] == login:
                if log_password[1] == hashpassword(login, password):
                    print("Вы ввели правильный пароль")
                else:
                    print("Вы ввели неправильный пароль")


def create_new_user():
    while True:
        login = input("Введите новый логин:")
        password = input("Введите новый пароль:")
        with open("DB.csv", 'r') as f:
            for line in f:
                log_password = line[:-1].split(',')
                if log_password[0] == login:
                    print("Пользователь уже существует")
                    break
            else:
                break
    with open("DB.csv", 'a') as f:
        with open("users_password(not_hashed).csv", 'a') as p:
            p.writelines(login + "," + password + '\n')
            f.writelines(login + "," + str(hashpassword(login, password)) + "\n")
            print("Пользователь успешно создан")
            print("В базе данных хранится строка:" + str(hashpassword(login, password)))
    return login


#createDB()
validation(create_new_user())

