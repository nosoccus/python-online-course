def palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]


if __name__ == "__main__":
    f = open("palindromes.txt", "r")
    for line in f:
        word = line.strip("\n")
        print(palindrome(word))
