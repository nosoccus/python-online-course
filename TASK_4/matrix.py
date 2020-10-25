my_list = []
temp_list = []
n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))
print("Please, input elements of matrix one by one")
# Заповнюємо нашу матрицю через консоль
for i in range(n):
    for j in range(m):
        temp_list.append(int(input()))
    my_list.append(temp_list)
    temp_list = []

print("Original matrix is: ")
for row in my_list :
    print(row)

# Транспонуємо
t_matrix = zip(*my_list)

print("\nTransposed matrix is: ")
for row in t_matrix:
    print(list(row))
