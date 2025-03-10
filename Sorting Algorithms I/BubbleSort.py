def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapping = False

        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                # swap arr[j] and arr[j - 1]
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapping = True
        if not swapping:
            break
    print(arr)


bubble_sort([4, 1, 5, 2, 7])
