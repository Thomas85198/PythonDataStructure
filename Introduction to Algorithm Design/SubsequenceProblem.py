def sub_sequence(sub_str, str):
    if len(sub_str) == 0:
        return True

    pt1 = 0
    pt2 = 0

    while (pt2 < len(str)):
        if str[pt1] == str[pt2]:
            pt1 += 1
        if pt1 >= len(sub_str):
            return True
        pt2 += 1

    return False


print(sub_sequence("hello", "hello Dear"))
