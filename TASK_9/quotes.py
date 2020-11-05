def rvrs(old_str: str):
    old_words = list(old_str.split(" "))
    new_words = []
    for word in old_words:
        new_words.append(word.translate(str.maketrans({"'": '"', '"': "'"})))
    new_str = ' '.join([str(word) for word in new_words])
    return new_str


if __name__ == "__main__":
    str1 = "\'frog\' and \"dog\""
    str2 = "\"There is quotes \'in quotes\'\""

    print("Old string: " + str1)
    print("New string: " + rvrs(str1), "\n")

    print("Old string: " + str2)
    print("New string: " + rvrs(str2))
