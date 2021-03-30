"""
    1. Вводится строка
    2. Программа считает количество слов в введенной строке и выводит на экран.
    2. Программа определяет самое длинное слово и его длину и выводит на экран.
    ___________________________________________________________________________

    Например:
###
     Hello,world! I am learning python.
###
    Слов в введенной строке: 6
    Самое длинное слово: "learning" (8 символов)

"""
string = input("Введіть текст:")
string = (
                string.replace(",", "")
                .replace(".", " ")
                .replace("!", " ")
                .replace("-", "")
                .replace("?", " ")
                )
words = string.split()
l = len(string)
count = 0
_max_ = 0
begin = 0
print("Кількість слів:", len(words))
for i in range(l):
    if string[i] != " ":
        count +=1
    else:
        if count > _max_:
            _max_ = count
            begin = i - count
        count = 0
print("Найдовше слово:", string[begin:begin+_max_])




