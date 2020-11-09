i = 0
res_list = [None]


def remember_result(func):
    def wrapper(*args, **kwargs):
        global res_list
        global i
        print(f"Last result = '{res_list[i]}'")
        curr = func(*args, **kwargs)
        res_list.append(curr)
        i += 1
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


if __name__ == "__main__":
    print(sum_list("a", "b"))
    print(sum_list("abc", "cde"))
    print(sum_list(3, 4, 5))
