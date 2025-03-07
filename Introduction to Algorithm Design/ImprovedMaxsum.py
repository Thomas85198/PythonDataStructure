
def max_sum(arr, k):

    if k > len(arr):
        return None

    max_value = 0

    for i in range(k):
        max_value += arr[i]

    temp_value = max_value
    for j in range(k, len(arr)):
        temp_value = temp_value + arr[j] - arr[j - k]
        if temp_value > max_value:
            max_value = temp_value

    print(max_value)
    return max_value


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


max_sum([2, 7, 3, 7, 25, 0, 6, 1, -5, -12, -11], 3)  # 12
min_sum([2, 7, 3, 0, 6, 1, -5, -12, -11], 3)  # -28
