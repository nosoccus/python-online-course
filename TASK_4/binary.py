def to_bin(n: int) -> str:
    if n <= 1:
        return "1" if n == 1 else "0"
    if n % 2 == 0:
        return to_bin(n/2) + "0"
    else:
        return to_bin((n-1)/2) + "1"


if __name__ == "__main__":
    n = int(input("Enter a decimal number: "))
    res = to_bin(n)
    print("Binary represination:", res)
    print("Sum is", sum(int(digit) for digit in res))
