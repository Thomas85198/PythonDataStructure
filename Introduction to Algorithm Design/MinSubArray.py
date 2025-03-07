def min_sub_array(arr, sum):
    left = 0
    right = 0
    min_length = float('inf')
    current_sum = 0

    while right < len(arr):
        current_sum += arr[right]

        while current_sum >= sum:
            # 更新 min_lenght 的值
            if min_length > (right - left + 1):
                min_length = (right - left + 1)
            current_sum -= arr[left]
            left += 1
        right += 1
    if min_length == float('inf'):
        return 0
    else:
        return min_length


print(min_sub_array([9, 8, 1, 4, 9, 5, 1, 2], 11))  # 2
