def checker(x: int) -> str:
    s = ""
    if x % 3 == 0:
        s += "Fizz"
    if x % 5 == 0:
        s += "Buzz"
    if s == "":
        s = x
    return s


if __name__ == "__main__":
    while True:
        number = int(input("Enter the number: "))
        if 0 < number < 100:
            print(checker(number))
        else:
            print("Your number is out of range [1, 100]")
            break
