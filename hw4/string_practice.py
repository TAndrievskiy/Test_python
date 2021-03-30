string = "Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry."

# 1. Удалить из строки символы ','.
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'


# 2. Найти индекс самой последней буквы 'i' в строке.
#    Результат: 54


# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6


# 4. Найти и вывести срез строки от 3 буквы 's' до 6 пробела.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов, вторым
#     параметром можно передать индекс, от которого делать поиск find('s', 12))


# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(",", "")
l = len(string)
count = 0
print("Результат:" +  string)
print("Результат:", string.rindex("i"))
for i in range(l):
    if string[i] == "i" or string[i] == "I" :
        count +=1
print("Результат:", count)
for i in range(l):


print("Результат:" + string[:int(l / 2)] * 3 + string[int(l / 2):])



