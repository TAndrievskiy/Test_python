"""
    Необходимо реализовать программу, которая принимает текст и удаляет из него
    все, что находится в скобочках "(", ")". Скобки могут быть вложенными.
    И выводит получившийся текст.
    ___________________________________________________________________________

    Например:

    Программа принимает текст(вводится с клавиатуры(с помощью input())),
    форматирует его(удаляет все скобочки(и их содержимое)) и выводит на экран.

    Результат:
    Программа принимает текст, форматирует его и выводит на экран.
"""
count = 0
string = input("Введіть текст:")
length = len(string)
string_format = ""
if string.count('(') != string.count(')'):
    print("Невірна кількість дужок")
else:
    for i in range(length):
        if string[i] == "(":
            count += 1
        elif count == 0:
            string_format += string[i]
        elif string[i] == ")":
            count -= 1
    print("Результат:" + string_format)
