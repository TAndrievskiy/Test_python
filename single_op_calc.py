"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""
try:
    n = int(input('Введіть значення n:'))
    operation = input('Введіть операцію(+,-,*,/):')
    sumary = 0
    mul = 1
    if operation == '+':
        for i in range(1, n + 1):
            i = int(input('Введіть числа:'))
            sumary += i
        print('Результат:', sumary)
        input("Continue? (Y/n) ")
    elif operation == '-':
        for i in range(1, n + 1):
            i = int(input('Введіть числа:'))
            sumary -= i
        print('Результат:', sumary)
    elif operation == '*':
        for i in range(1, n + 1):
            i = int(input('Введіть числа:'))
            mul *= i
        print('Результат:', mul)
    elif operation == '/':
        i /= i
        print('Результат:', i)
    else:
        print('Не доступна операція!')
    if input("Continue? (Y/n) ") == "n":
        break
except ZeroDivisionError:
    print('На нуль ділити не можна!')
except ValueError:
    print("Введено невірне значення")


