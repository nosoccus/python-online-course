allow = True
res = 0


def call_once(func):
    def wrapper(*args, **kwargs):
        global allow
        global res
        if allow:
            res = func(*args, **kwargs)
            allow = False
        return res
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))
