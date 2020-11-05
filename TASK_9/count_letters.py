from collections import Counter


def f1(string):
    count = Counter(string)
    return count


def f2(string):
    dict = {}
    for value, key in enumerate(string):
        if dict.get(key) is None:
            dict[key] = 1
        else:
            dict[key] += 1
    return dict


if __name__ == "__main__":
    s = "Наївний баєсів класифікатор — ймовірнісний класифікатор, "
    "що використовує теорему Баєса для визначення ймовірності "
    "приналежності спостереження (елемента вибірки) до одного з класів "
    "при припущенні (наївному) незалежності змінних."
    print(f1(s), "\n")
    print(f2(s))
