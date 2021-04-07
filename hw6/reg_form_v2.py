"""
    Модифицируйте форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""

import string

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    file_path_users = BASE_DIR / "files" / "users.txt"
    users_file = open(file_path_users, "a+")
    number = get_phone_number()
    mail = get_email()
    password = get_password()
    print(
        "Congratulations on your successful registration!\n"
        f"Your phone number: {number}\n"
        f"Your email: {mail}\n"
        f"Your password: {password}\n"
    )
    print(f"Phone number:{number}, email:{mail}, password:{password}", file=users_file)
    users_file.close()


def error_file(error):
    file_path_errors = BASE_DIR / "files" / "errors.txt"
    errors_file = open(file_path_errors, "a+")
    print(error, file=errors_file)
    errors_file.close()


def get_phone_number():
    number = input("Enter phone number:")
    number = (
        number.replace("-", "")
              .replace(" ", "")
              .replace("+", "")
              .replace("-", "")
              .replace("(", "")
              .replace(")", "")
    )
    if number.isdigit() is False:
        print('Incorrect number')
        error_file("Invalid phone:" + number)
        return get_phone_number()
    elif len(number) < 9 or len(number) > 13:
        print("Incorrect length number")
        error_file("Invalid phone:" + number)
        return get_phone_number()
    elif number.isdigit() and len(number) >= 10:
        number = '+38' + number[len(number) - 10:]
        return number


def get_email():
    mail = input("Enter email:")
    if len(mail) < 6:
        print('Incorrect email')
        error_file("Invalid email:" + mail)
        return get_email()
    elif mail.count("@") != 1:
        print('Incorrect email')
        error_file("Invalid email:" + mail)
        return get_email()
    else:
        mail = mail.lower()
        return mail


def get_password():
    password = input("Enter password:")
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    if len(password) < 8:
        print('Password is too short')
        error_file("Invalid password:" + password)
        return get_password()
    elif password.isspace():
        print('Password must be without spaces')
        error_file("Invalid password:" + password)
        return get_password()
    for i in password:
        if i.isdigit():
            count_1 += 1
        elif i.isupper():
            count_2 += 1
        elif i.islower():
            count_3 += 1
        elif i in string.punctuation:
            count_4 += 1
    if count_1 * count_2 * count_3 * count_4 == 0:
        print("Password does not meet all requirements. Try again!")
        error_file("Invalid password:" + password)
        return get_password()
    else:
        return password_is_correct(password)


def password_is_correct(password):
    repeat_pass = input("Confirm your password:")
    if repeat_pass == password:
        for i in repeat_pass:
            repeat_pass = repeat_pass.replace(i, "*")
        return repeat_pass
    else:
        print("Password does not matches. Try again!")
        return get_password()


if __name__ == "__main__":
    main()