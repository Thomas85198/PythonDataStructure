nums = [-11, 0, 1, 2, 3, 9, 14, 17, 21]
avg = 1.5


def average_pair(lst, avg):
    left = 0
    right = len(nums) - 1
    result = []

    while (right > left):
        temp_avg = (lst[right] + lst[left]) / 2
        if (temp_avg > avg):
            right -= 1
        elif (temp_avg < avg):
            left += 1
        elif (temp_avg == avg):
            result.append([lst[left], lst[right]])
            left += 1
            right -= 1
        else:
            return -1
    print(result)
    return result


average_pair(nums, avg)
