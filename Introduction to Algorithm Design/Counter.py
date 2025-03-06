arr1 = [15, 3, 6, 8, 24, 16]
arr2 = [11, 3, 9, 6, 15, 8]


def counter(arr1, arr2):
    result = []
    counter = {}
    arr3 = arr1 + arr2
    for i in range(len(arr3)):
        if arr3[i] in counter:
            counter[arr3[i]] += 1
        else:
            counter[arr3[i]] = 1
    print(counter)

    for key, value in counter.items():
        if value > 1:
            result.append(key)
    print(result)


counter(arr1, arr2)
