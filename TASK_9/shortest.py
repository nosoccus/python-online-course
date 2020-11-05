def get_shortest_word(str1):
    word = ""
    all_words = []
    str1 += " "
    for i in range(0, len(str1)):
        if(str1[i] != " "):
            word = word + str1[i]
        else:
            all_words.append(word)
            word = ""

    small = all_words[0]

    for k in range(0, len(all_words)):
        if(len(small) > len(all_words[k])):
            small = all_words[k]
    return small


str1 = "Write program to sort an array of given integers using Quick sort."
print("String:", str1)
print("Shortest word:", get_shortest_word(str1))
