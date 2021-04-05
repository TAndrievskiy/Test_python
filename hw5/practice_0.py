"""
    Напишите функцию, которая не принимает водных параметров,
    запрашивает у пользователя username, валидирует его и возвращает.

    Валидации:
    - мимимальное количество символов 6 (len)
    - максимальное количество симолов 20 (len)
    - доступны только латинские буквы в нижнем регистре и _ (in, string lib)
    - username не может начинаться символом _ (.startswith())

    Если какое-то из требований не выполняется, запрашиваем повторный ввод.

    * смотрите lesson5/_6_practice_valid.py
"""

import string


def main():
    while True:
        print("Enter username:", end=" ")
        login = input()
        username = get_username(login)
        if get_username(login):
            print(f"Hi, {username}!")
            break
        else:
            print("Try again!")
            continue


def get_username(login) -> str:
    for i in login:
        if 6 > len(login):
            return False
        elif 20 < len(login):
            return False
        elif login.startswith("_"):
            return False
        elif i in string.ascii_uppercase:
            return False
        elif i in string.digits:
            return False
        elif i in string.punctuation:
            if i == '_':
                continue
            else:
                return False
    else:
        return login


if __name__ == "__main__":
    main()
