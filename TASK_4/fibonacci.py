def rec_fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return(rec_fibo(n-1) + rec_fibo(n-2))


if __name__ == "__main__":
    n = int(input("Please, enter the length of sequence: "))
    fibo_list = []
    if n > 0:
        for i in range(n):
            fibo_list.append(rec_fibo(i))
        print("Fibonacci sequence:", fibo_list)
        print("Sum of elements in Fibonacci sequence:", sum(fibo_list))
    else:
        print("Plese enter a positive integer")
