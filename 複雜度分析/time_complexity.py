def constant(n: int) -> int:
    """ 常數階 """
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count


def linear(n: int) -> int:
    """ 線性階 """
    count = 0
    for _ in range(n):
        count += 1
    return count


def array_traversal(nums: list[int]) -> int:
    """ 線性階(走訪陣列) """
    count = 0
    for num in nums:
        count += 1
    return count


def quadratic(n: int) -> int:
    """ 平方階 """
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def bubble_sort(nums: list[int]) -> int:
    """ 平方階(泡沫排序)"""
    count = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp: int = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3
    return count


def exponential(n: int) -> int:
    """ 指數階(迴圈實現) """
    count = 0
    base = 1
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    return count


def exp_recur(n: int) -> int:
    """ 指數階(遞迴實現) """
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1


def logarithmic(n: int) -> int:
    """ 對數階(迴圈實現) """
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count


def log_recur(n: int) -> int:
    """ 對數階(遞迴實現) """
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1


def linear_log_recur(n: int) -> int:
    """ 線性對數階 """
    if n <= 1:
        return 1
    count = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count


def factorial_recur(n: int) -> int:
    """ 階乘階(遞迴實現) """
    if n == 0:
        return 1
    count = 0
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count
