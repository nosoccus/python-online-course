import issorted as ss


def transform(nums, sort_order):
    mod_list = []
    if ss.is_sorted(nums, sort_order):
        for i in range(len(nums)):
            mod_list.append(nums[i] + i)
    return mod_list


if __name__ == "__main__":
    nums = list(map(int, input("Enter a list: ").split()))
    order = int(input("Choose order (1 - descending | 2 - ascending): "))

    if order == 1:
        print("New list:", transform(nums, ss.Guider.descending))
    elif order == 2:
        print("New list:", transform(nums, ss.Guider.ascending))
