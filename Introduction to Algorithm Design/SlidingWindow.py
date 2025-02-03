arr = [2, 7, 3, 0, 6, 1, -5, -12, -11]
window_size = 3


def max_sum(arr, size):

    max = float('-inf')

    if (size > len(arr)):
        return None
    for i in range(len(arr) - size + 1):
        window = []
        attempt = 0
        for j in range(i, i + size):
            attempt += arr[j]
        if attempt > max:
            max = attempt
    return max

def max_sum_imprve(arr, size):
    max = float('-inf')

    if (size > len(arr)):
        return None
    for i in range(len(arr) - size + 1):
        window = []
        attempt = 0
        for j in range(i, i + size):
            attempt += arr[j]
        if attempt > max:
            max = attempt
    return max


def min_sum(arr, size):
    min = float('inf')

    if (size > len(arr)):
        return None
    for i in range(len(arr) - size + 1):
        window = []
        attempt = 0
        for j in range(i, i + size):
            attempt += arr[j]
        if attempt < min:
            min = attempt
    return min


print(max_sum(arr, window_size))
print(min_sum(arr, window_size))
