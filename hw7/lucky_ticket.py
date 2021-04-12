"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
    Если количество цифр одной и второй половины не равно - билет не счастливый
"""


def main():
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


def is_lucky(ticket_num) -> bool:
    ticket = str(ticket_num)
    centre = len(ticket) // 2
    sum_1 = 0
    sum_2 = 0
    if len(ticket) % 2 != 0:
        print("Unlucky..(")
        return False
    for i in ticket[:centre]:
        sum_1 += int(i)
    for j in ticket[centre:]:
        sum_2 += int(j)
    if sum_1 == sum_2:
        print("Lucky ticket!!!")
        return True
    else:
        print("Unlucky..(")
        return False


if __name__ == "__main__":
    main()
