arr1 = [15, 3, 6, 8, 24, 16]
arr2 = [11, 3, 9, 6, 15, 8]


def intersection_problem(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                result.append(arr2[j])
    print(result)
    return result


intersection_problem(arr1, arr2)
