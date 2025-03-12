arr = [15, 3, 17, -17, 3.1415, 18, 20, 2, 1, 666]


def partition(p, r):
    x = arr[r]  # pivot
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # swap arr[i + 1] and arr[r]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1


def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q - 1)
        quick_sort(q + 1, r)


quick_sort(0, len(arr) - 1)
print(arr)
