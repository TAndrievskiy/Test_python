"""
    Реализовать программу, с помощью которой можно (меню):
    1. Найти наибольшую цифру числа n.
    2. Найти количество четных и нечетных цифр в числе n.
    3. Узнать, является ли число n простым.
    4. Отобразить ряд простых чисел от 2 до n через запятую.
"""

try:
    while True:
        print(
            "1. Найти наибольшую цифру числа n.",
            "2. Найти количество четных и нечетных цифр в числе n.",
            "3. Узнать, является ли число n простым.",
            "4. Отобразить ряд простых чисел от 2 до n через запятую.",
            "5. Выход.",
            sep="\n",
        )
        menu_item = input("Выберите пункт меню: ")
        if menu_item == "1":
            n = int(input("Enter n: "))
            a = n % 10
            n = n // 10
            while n > 0:
                if n % 10 > a:
                    a = n % 10
                n = n // 10
            print("Наибольшая цифра:", a)
        elif menu_item == "2":
            n = int(input("Enter n: "))
            odd = 0
            even = 0
            while n > 0:
                if n % 2 == 0:
                    even += 1
                else:
                    odd += 1
                n = n // 10
            print("even:", even, "odd:", odd)
        elif menu_item == "3":
            n = int(input("Enter n: "))
            if n > 2:
                for i in range(2, n):
                    if n % i == 0:
                        print("n isn`t simple")
                        break
                else:
                    print("n is simple")
            elif n < 0:
                print("Enter correct value")
            else:
                print("n is simple")
        elif menu_item == "4":
            n = int(input("Enter n: "))
            if n < 2:
                print("Enter correct value")
            else:
                for a in range(2, n + 1):
                    for b in range(2, a + 1):
                        if a % b == 0:
                            if a == b:
                                print(a, "", sep=",", end="")
                            break
                print()
        elif menu_item == "5":
            print("Bye!")
            break
except ValueError:
        print("Value not correct")
