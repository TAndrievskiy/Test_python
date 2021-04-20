"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""

from collections import Counter


def main():
    text = input("Enter text:")
    frequent_word(text)


def frequent_word(text):
    text = text.split()
    new_text = sorted(text, key=str.lower)
    counter = Counter(new_text)
    print(counter.most_common(1))


if __name__ == "__main__":
    main()
