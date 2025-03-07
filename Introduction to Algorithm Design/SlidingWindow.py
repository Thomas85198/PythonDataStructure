
def max_sum(arr, k):
    max_value = float('-inf')

    if k > len(arr):
        return None

    for i in range(len(arr) - k + 1):
        attempt = 0

        for j in range(i, i + k):
            attempt += arr[j]
        if attempt > max_value:
            max_value = attempt

    print(max_value)


def min_sum(arr, k):
    min_value = float('inf')

    if k > len(arr):
        return None

    for i in range(len(arr) - k + 1):
        attempt = 0
        for j in range(i, i + k):
            attempt += arr[j]
        if attempt < min_value:
            min_value = attempt
    print(min_value)


max_sum([2, 7, 3, 0, 6, 1, -5, -12, -11], 3)  # 12
min_sum([2, 7, 3, 0, 6, 1, -5, -12, -11], 3)  # -28
