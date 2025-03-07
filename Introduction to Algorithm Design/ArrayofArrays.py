arrs = [[[["a", [["b", ["c"]], ["d"]]], [["e"]], [[["f", "g", "h"]]]]]]


def collector(arr1):
    result = []

    def helper(arr2):
        for i in range(len(arr2)):
            if isinstance(arr2[i], list):
                helper(arr2[i])
            else:
                result.append(arr2[i])
    helper(arr1)
    return result


print(collector(arrs))
