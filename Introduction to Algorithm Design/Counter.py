# 解法一
from collections import Counter

arr_1 = [15, 3, 6, 8, 24, 16]
arr_2 = [11, 3, 9, 6, 15, 8]

counter1 = Counter(arr_1)
counter2 = Counter(arr_2)
intersection = counter1.keys() & counter2.keys()

print(intersection)


# 解法二
def find_intersection_counter(arr1, arr2):
    counter = {}

    for num in arr1:
        counter[num] = counter.get(num, 0) + 1

    result = []
    for num in arr2:
        if num in counter:
            result.append(num)

    return list(result)


print(find_intersection_counter(arr_1, arr_2))
