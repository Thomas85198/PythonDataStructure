nums = [-11, 0, 1, 2, 3, 9, 14, 17, 21]
avg = 1.5


def average_pair(lst, avg):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if ((lst[i] + lst[j]) / 2) == avg:  # 正確計算平均值 == avg)
                result.append([nums[i], nums[j]])
    print(result)


average_pair(nums, avg)
