arr = [2, 7, 3, 0, 6, 1, -5, -12, -11]
window_size = 3


def max_sum_improved(arr, size):
    if size > len(arr):
        return None

    # 初始化窗口和
    current_sum = sum(arr[:size])
    max_sum = current_sum

    # 滑動窗口
    for i in range(size, len(arr)):
        # 移除最早的元素，添加新的元素
        current_sum += arr[i] - arr[i - size]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


# 測試
print(max_sum_improved(arr, window_size))
