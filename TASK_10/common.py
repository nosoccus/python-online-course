from collections import Counter


def most_common_words(filename, num_words):
    with open(filename) as fin:
        cnt = Counter(fin.read().strip().split())
    return cnt.most_common(num_words)


if __name__ == "__main__":
    num = int(input("Enter number or words to print: "))
    print(most_common_words('lorem_ipsum.txt', num))
