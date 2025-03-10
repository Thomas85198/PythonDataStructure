def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (i >= 0) and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    print(arr)
    return arr


unsorted = [14, -4, 17, 6, 22, 1, -5]
insertion_sort(unsorted)
