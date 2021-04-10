"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
    Если количество цифр одной и второй половины не равно - билет не счастливый
"""


def is_lucky(ticket_num: int) -> bool:
    ticket_num = list()
    centre = len(ticket_num) // 2
    if sum(ticket_num[:centre]) == sum(ticket_num[centre:]):
        print("Lucky ticket!!!")
        return True
    else:
        print("Unlucky..(")
        return False


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
assert is_lucky(4799731) is False
assert is_lucky(1379974) is False

print("All tests passed successfully!")