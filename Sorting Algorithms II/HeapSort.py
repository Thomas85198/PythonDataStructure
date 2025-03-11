def build_max_heap(arr, heapSize):
    for i in range(heapSize // 2, -1, -1):
        max_heapify(arr, i, heapSize)


def max_heapify(arr, i, heapSize):
    largest: int
    l = i * 2 + 1
    r = i * 2 + 2
    if l <= heapSize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        # swap arr[i] with arr[largest]
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heapSize)


def heap_sort(arr):
    heapSize = len(arr) - 1
    build_max_heap(arr, heapSize)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapSize -= 1
        max_heapify(arr, 0, heapSize)
    return arr


arr = [15, 3, 17, 18, 20, 2, 1, 666]
heap_sort(arr)
print(arr)
