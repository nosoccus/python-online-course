CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1]


def play(first_card: str, second_card: str) -> str:
    sum_value = VALUES[CARDS.index(first_card)] + \
                VALUES[CARDS.index(second_card)]
    return sum_value % 10


if __name__ == "__main__":
    first_card = str(input("Play first card: "))
    second_card = str(input("Play second card: "))

    if first_card in CARDS and second_card in CARDS:
        print("Your result:", play(first_card, second_card))
    else:
        print("Your result: Do not cheat!")
