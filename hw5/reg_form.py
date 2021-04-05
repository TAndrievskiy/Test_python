"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)

"""
import string


def main():
    number = get_phone_number()
    mail = get_email()
    password = get_password()
    print(
        "Congratulations on your successful registration!\n"
        f"Your phone number: {number}\n"
        f"Your email: {mail}\n"
        f"Your password: {password}\n"
    )


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
        return get_phone_number()
    elif len(number) < 9 or len(number) > 13:
        print("Incorrect length number")
        return get_phone_number()
    elif number.isdigit() and len(number) >= 10:
        number = '+38' + number[len(number) - 10:]
        return number


def get_email():
    mail = input("Enter email:")
    if len(mail) < 6:
        print('Incorrect email')
        return get_email()
    elif mail.count("@") != 1:
        print('Incorrect email')
        return get_email()
    else:
        mail = mail.lower().strip
        return mail


def get_password():
    password = input("Enter password:")
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    if len(password) < 8:
        print('Password is too short')
        return get_password()
    elif password.isspace():
        print('Password must be without spaces')
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
