nums = [-11, 0, 1, 2, 3, 9, 14, 17, 21]
average_nums = 1.5


def average_pair(arr, avg_nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(f"{arr[i]}, vs {arr[j]} 平均是: {arr[i] + arr[j] / 2}")
            if (arr[i] + arr[j]) / 2 == avg_nums:
                result.append([arr[i], arr[j]])
    print(result)


average_pair(nums, average_nums)
