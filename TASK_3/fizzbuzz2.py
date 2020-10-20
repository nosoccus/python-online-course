def checker(x: int) -> str:
    fizz = "" if x % 3 else "Fizz"
    buzz = "" if x % 5 else "Buzz"
    return fizz + buzz if fizz or buzz else x


if __name__ == "__main__":
    while True:
        number = int(input("Enter the number: "))
        if 0 < number < 100:
            print(checker(number))
        else:
            print("Your number is out of range [1, 100]")
            break
