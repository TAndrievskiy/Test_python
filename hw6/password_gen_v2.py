"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:

    1. Все сгенерированные пароли записывались в файл passwords.txt
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".

    3*. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.

    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается

"""
import string
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


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


def generated_pass_library(passwords):
    file_path = BASE_DIR / "files" / "passwords.txt"
    with open(file_path, "a+") as f:
        print(passwords, file=f)
    with open(file_path, "r") as f:
        saved_pass = f.read()
        if saved_pass.count(passwords) > 1:
            print("Insecure pass")


def generate_simple_pass():
    pass_len = is_correct_length()
    password = ""
    for i in range(pass_len):
        password += random.choice(string.ascii_lowercase)
    print(f"Generated password: {password}")
    generated_pass_library("Simple password:" + password)
    return password


def generate_medium_pass():
    pass_len = is_correct_length()
    password = ""
    for i in range(pass_len):
        password += random.choice(string.ascii_letters + string.digits)
    print(f"Generated password: {password}")
    generated_pass_library("Medium password:" + password)
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
    generated_pass_library("Hard password:" + password)
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