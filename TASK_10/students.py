import pandas as pd


def get_top_performers(df, num):
    df = df.sort_values(by="average mark", ascending=False)
    return df["student name"].head(num)


def write_sort_desc(df, column):
    df = df.sort_values(by=column, ascending=False)
    df.to_csv("students_by_age.csv", index=False)
    return "Writed to a file."


def head_age_desc(num):
    df = pd.read_csv("students_by_age.csv")
    return df.head(num)


if __name__ == "__main__":
    data = pd.read_csv("students.csv")
    print("Top students by average mark:\n", get_top_performers(data, 5))
    print(write_sort_desc(data, "age"))
    print("Students by age:\n", head_age_desc(5))
