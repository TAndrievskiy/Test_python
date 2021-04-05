"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

import string
import random


def main():
    choice = input(
        "Password generator \n"
        "1. Generate simple password.\n"
        "2. Generate medium password.\n"
        "3. Generate hard password.\n"
        "4. Exit.\n"
        "Chose and press Enter: "
    )
    if choice == "1":
        generate_simple_pass()
    elif choice == "2":
        generate_medium_pass()
    elif choice == "3":
        generate_hard_pass()
    elif choice == "4":
        print("Bye!")
        return

    return main()


def generate_simple_pass():
    pass_len = is_correct_length()
    password = ""
    for i in range(pass_len):
        password += random.choice(string.ascii_lowercase)
    print(f"Generated password: {password}")
    return password


def generate_medium_pass():
    pass_len = is_correct_length()
    password = ""
    for i in range(pass_len):
        password += random.choice(string.ascii_letters + string.digits)
    print(f"Generated password: {password}")
    return password


def auto_generation_hard_pass():
    length = random.randint(8, 16)
    return length


def generate_hard_pass():
    choice = input(
        "1. Autogenerate password.\n"
        "2. Custom length and generate password.\n"
        "Chose and press Enter: "
    )
    if choice == "1":
        hard_pass_len = auto_generation_hard_pass()
    elif choice == "2":
        hard_pass_len = is_correct_hard_length()
    password = ""
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    for i in range(hard_pass_len):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        for j in password:
            if j in string.ascii_uppercase:
                count_1 += 1
            elif j in string.ascii_lowercase:
                count_2 += 1
            elif j in string.digits:
                count_3 += 1
            elif j in string.punctuation:
                count_4 += 1
    if count_1 * count_2 * count_3 * count_4 == 0:
        print("Generated password does not meet all requirements. Try again!")
        return generate_hard_pass()
    print(f"Generated password: {password}")
    return password


def is_correct_length() -> int:
    length = is_int_length()
    if 0 < length < 8:
        print("Warning! Password is too short!")
        return length
    elif length == 8:
        return length
    else:
        print("Incorrect length!")
        return is_correct_length()


def is_correct_hard_length() -> int:
    length = is_int_length()
    if 7 < length < 17:
        return length
    else:
        print("Incorrect length!")
        return is_correct_hard_length()


def is_int_length():
    try:
        length = int(input("Enter the pass length:"))
        return length
    except ValueError:
        print("Incorrect value!")
        return is_int_length()


if __name__ == "__main__":
    main()



