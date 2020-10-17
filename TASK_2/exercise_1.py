def count_negatives(numbers: list) -> int:
    cnt = len(list(filter(lambda x: x < 0, numbers)))
    return cnt


if __name__ == "__main__":
    input_numbers = [4, -9, 8, -11, 8]
    print(f"There are {count_negatives(input_numbers)} negative numbers in the list {input_numbers}")
