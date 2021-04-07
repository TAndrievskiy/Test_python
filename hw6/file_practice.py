"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""
"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""
"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""
"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""
"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    """1"""
    file_path = BASE_DIR / "file_practice.txt"
    with open(file_path, "w") as f:
        print("Starting practice with files\n", file=f)
    """2"""
    with open(file_path, "r") as f:
        first_5 = f.read(5).upper()
        f.seek(0)
        print(first_5 + f.read())
    """3"""
    file_path_2 = BASE_DIR / "files" / "text.txt"
    with open(file_path_2, "r+") as f:
        text = f.read()
        if text.count("i") > text.count("e"):
            text = text.replace("i", "e")
        else:
            text = text.replace("e", "i")
        f.close()
    with open(file_path, "a+") as f:
        print(text, file=f)
    """4"""
    with open(file_path, "a+") as f:
        f.read()
        if len(f.read()) % 2 == 0:
            print("the end\n", file=f)
        else:
            print("bye\n", file=f)
        f.seek(0)
        print(f.read())
    """5"""
    with open(file_path, "r") as f:
        practice = f.read()
    with open(file_path, "w") as f:
        print(practice[:len(practice) // 2], file=f)
        print(" *some inserted text* ", file=f)
        print(practice[len(practice) // 2:], file=f)


if __name__ == "__main__":
        main()