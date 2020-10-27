from enum import Enum


class Guider(Enum):
    descending = 1
    ascending = 0


def is_sorted(nums: list, sort_order: Enum):
    flag = 0

    if sort_order == Guider.descending:
        if all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)):
            flag = 1
    elif sort_order == Guider.ascending:
        if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
            flag = 1

    if flag:
        return True
    else:
        return False


if __name__ == "__main__":
    nums = list(map(int, input("Enter a list: ").split()))
    order = int(input("Choose order (1 - descending | 2 - ascending): "))
    
    if order == 1:
        print("List is sorted:", is_sorted(nums, Guider.descending))
    elif order == 2:
        print("List is sorted:", is_sorted(nums, Guider.ascending))
