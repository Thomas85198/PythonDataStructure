import random


def random_numbers(n: int) -> list[int]:
    """ 生成一個陣列，元素為: 1, 2, ..., n，順序被打亂 """
    nums = [i for i in range(1, n + 1)]
    random.shuffle(nums)
    return nums


def find_one(nums: list[int]) -> int:
    """ 查詢陣列 nums 中數字 1 所在索引 """
    for i in range(len(nums)):
        if nums[i] == 1:
            return i
    return - 1
