from collections import Counter
import string


def most_common_words(filename, num_words):
    with open(filename) as rf:
        cnt = Counter(rf.read().lower().translate(
            str.maketrans('', '', string.punctuation)).strip().split())
    return cnt.most_common(num_words)


if __name__ == "__main__":
    num = int(input("Enter number or words to print: "))
    print(most_common_words('lorem_ipsum.txt', num))
