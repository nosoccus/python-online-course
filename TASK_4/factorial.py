def loop_method(n: int) -> int:
    fct = 1
    for i in range(1, n + 1):
        fct = fct * i
    return fct


def rec_method(n: int) -> int:
    if n in (0, 1):
        return 1
    else:
        return n * rec_method(n-1)


if __name__ == "__main__":
    n = int(input("Input a number for factorial: "))
    if n >= 0:
        print("Calculated value by loop:     ", loop_method(n))
        print("Calculated value by recursion:", rec_method(n))
    else:
        print("Sorry, factorial does not exist for negative numbers")
