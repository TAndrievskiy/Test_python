"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.

    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""


def longest_strings(list_in: list) -> list:
    """ Функция возвращает список самых длинных строк из списка list_in """
    longest_string = list()
    max_len = 0
    for string in list_in:
        if len(string) > max_len:
            max_len = len(string)
    for string in list_in:
        if len(string) == max_len:
            longest_string.append(string)
    return longest_string


t_1 = ["x"]
assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]

t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]

print("All tests passed successfully!")
