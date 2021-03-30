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
    while True:
        n = int(input('Введіть значення n:'))
        operation = input('Введіть операцію(+,-,*,/):')
        result = 0
        while n > 0:
            i = int(input('Введіть числа:'))
            result = i
            if operation == '+':
                for i in range(n - 1):
                    i = int(input('Введіть числа:'))
                    result += i
                print('Результат:', result)
            elif operation == '-':
                for i in range(n - 1):
                    i = int(input('Введіть числа:'))
                    result -= i
                print('Результат:', result)
            elif operation == '*':
                for i in range(n - 1):
                    i = int(input('Введіть числа:'))
                    result *= i
                print('Результат:', result)
            elif operation == '/':
                for i in range(n - 1):
                    i = int(input('Введіть числа:'))
                    result /= i
                print('Результат:', result)
            else:
                print('Не доступна операція!')
            if input("Continue? (Y/n) ") == "Y":
                break
            else:
                print("Bye!")
                exit()
        else:
            print("Невірне значення")
except ZeroDivisionError:
    print('На нуль ділити не можна!')
except ValueError:
    print("Введено невірне значення")


