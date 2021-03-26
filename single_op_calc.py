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
    x = int(input('Введіть числа:'))
    if operation == '+':
        for i in range(1, n):
            i = int(input('Введіть числа:'))
            result = x + i
        print('Результат:', result)
        input("Continue? (Y/n) ")
    elif operation == '-':
        for i in range(1, n):
            i = int(input('Введіть числа:'))
            i -= i
        print('Результат:', i)
    elif operation == '*':
        for i in range(1, n):
            i = int(input('Введіть числа:'))
            i *= i
        print('Результат:', i)
    elif operation == '/':
        i /= i
        print('Результат:', i)
    else:
        print('Не доступна операція!')
except ZeroDivisionError:
    print('На нуль ділити не можна!')
except ValueError:
    print("Введено невірне значення")

