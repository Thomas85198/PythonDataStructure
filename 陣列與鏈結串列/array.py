import random
arr: list[int] = [0] * 5
nums: list[int] = [1, 3, 2, 5, 4]


def random_access(nums: list[int]) -> int:
    """ 隨機訪問元素 """
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num


def insert(nums: list[int], num: int, index: int):
    """ 在陣列的索引 index 處插入元素 num """
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num


def remove(nums: list[int], index: int):
    """ 刪除索引 index 處的元素 """
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]


def traverse(nums: list[int]):
    """ 走訪陣列 """
    count = 0
    for i in range(len(nums)):
        count += nums[i]
    for num in nums:
        count += num
    for i, num in enumerate(nums):
        count += nums[i]
        count += num


def find(nums: list[int], target: int) -> int:
    """ 在陣列中查詢指定元素 """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return - 1


def extend(nums: list[int], enlarge: int) -> list[int]:
    """ 擴展陣列長度 """
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]

    return res
