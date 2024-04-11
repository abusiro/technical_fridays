def is_palindrome() -> bool:
    """
    Esta función devuelve True si la cadena es un palíndromo y False en caso contrario.
    :return:
    """
    string = input("Enter a word to check if it is a palindrome: ")
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def is_palindrome2(string: str = 'marypoppins') -> bool:
    """
    Esta función devuelve True si la cadena es un palíndromo y False en caso contrario.
    :param string:
    :return:
    """

    _reversed = ""
    for i in string:
        _reversed = i + _reversed
    return True if string == _reversed else False



def consecutive_zeros(string):
    count = 0
    max_count = 0
    for i, digit in enumerate(string):
        if digit == 0:
            count += 1
        elif digit == 1 and count != 0:
            max_count = count if count > max_count else max_count
            count = 0
    return max_count


def swap_keys_and_values(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict


if __name__ == '__main__':
    print('swap keys and values {"a": 1, "b": 2, "c": 3}')
    print(swap_keys_and_values({'a': 1, 'b': 2, 'c': 3}))
    print('consecutive zeros')
    print(consecutive_zeros('10010001'))
    print('is marypoppins a palindrome?')
    print(is_palindrome2())