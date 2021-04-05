"""
    Программу принимает на ввод строку string и число n.
    Выводит на экран строку с смещенными символами на число n.

    Весь код можно написать в одной функции main,
    но рекомендуется разбить код на несколько функций, например:
    - main
    - функция для получения не пустой строки.
    - функция для получения сдвига (целое число).
    - функция, которая делает сдвиг строки.

    Пример:
    Введите строку: python hello world
    Введите сдвиг: 5

    Результат: n hello worldpytho

    Введите строку: python hello world
    Введите сдвиг: -2

    Результат: ldpython hello wor

    * используйте индексы, срезы и возможно циклы
"""


def main():
    text = get_text()
    shift = get_shift_num()
    shift_perform(text, shift)


def get_text():
    text = input("Type the text:")
    if len(text) == 0:
        print("Incorrect value!")
        return get_text()
    else:
        return text


def get_shift_num():
    try:
        shift = int(input("Enter shift:"))
        return shift
    except ValueError:
        print("Incorrect value!")
        return get_shift_num()


def shift_perform(text, shift):
    shift_text = ""
    for i in range(len(text)):
        shift_text = text[shift:] + text[:shift]
    print(f"Result: {shift_text}")
    return shift_text


if __name__ == "__main__":
    main()
