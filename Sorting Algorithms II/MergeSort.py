def merge(a1, a2):
    result = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] > a2[j]:
            result.append(a2[j])
            j += 1
        else:
            result.append(a1[i])
            i += 1
    # a1 or a2 might have some elements left
    while i < len(a1):
        result.append(a1[i])
        i += 1
    while j < len(a2):
        result.append(a2[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = arr[0:middle]
        right = arr[middle:len(arr)]
        return merge(merge_sort(right), merge_sort(left))


print(merge([1, 15, 17], [-3, 9, 16]))
unsorted = [15, 3, 17, 18, 35, 11, 0, 36]
print(merge_sort(unsorted))
