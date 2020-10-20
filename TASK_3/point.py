def validate_point(x: float, y: float) -> bool:
    if 0 <= y <= 1 and abs(x) <= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Is point in shadow area:", validate_point(x, y))
