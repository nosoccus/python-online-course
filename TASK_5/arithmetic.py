def progression(a, d, n) -> list:
    nums = []
    nums.append(a)
    for i in range(n-1):
        a += d
        nums.append(a)
    return nums


def mult(nums) -> int:
    res = 1
    for i in nums:
        res *= i
    return res

if __name__ == "__main__":
    a, d, n = map(int, input("Please, enter a, d, n: ").split())
    nums = progression(a, d, n)
    print("Progression:", nums)
    print("Production:", mult(nums))
