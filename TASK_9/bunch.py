import string


def f1(*strings):
    strings = list(map(set, strings[0]))
    return strings[0].intersection(*strings)


def f2(strings):
    common_string = ''.join(strings)
    return set(common_string.lower())


def f3(strings):
    sets = []
    for i in range(len(strings)):
        sets.append(set(strings[i].lower()))

    list_common_letters = []
    for i in range(len(sets) - 1):
        result = sets[i].intersection(sets[i + 1])
        list_common_letters.append(result)

    result = set()
    for value in list_common_letters:
        result |= value

    return result


def f4(strings):
    alphabet = set(string.ascii_lowercase)
    s = ''.join(strings)
    letters = set(s.lower())
    return alphabet.difference(letters)


if __name__ == '__main__':
    strings = input("Enter your string: ").split()
    print("Function 1:", f1(strings))
    print("Function 2:", f2(strings))
    print("Function 3:", f3(strings))
    print("Function 4:", f4(strings))
