def selection_sort(arr):
    for i in range(len(arr) - 1):  # 最後一個元素最後應該被排好了，所以不用跑
        print(i)
        print(arr)
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    # print(arr)
    return arr


undorted = [14, -4, 17, 6, 22, 1, -5]
selection_sort(undorted)
