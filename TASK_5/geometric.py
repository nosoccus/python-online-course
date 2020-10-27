def progression(b, q, lim) -> list:
    nums = []
    nums.append(b)
    while b > lim:
        b *= q
        if b > lim:
            nums.append(b)
    return nums


def mult(nums) -> float:
    res = 0
    for i in nums:
        res += i
    return res


if __name__ == "__main__":
    b, q, lim = map(float, input("Please, enter b, q, lim: ").split())
    nums = progression(b, q, lim)
    print("Progression:", nums)
    print("Sum:", mult(nums))
