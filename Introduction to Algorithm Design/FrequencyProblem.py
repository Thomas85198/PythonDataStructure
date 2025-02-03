str_1 = "abbc"
str_2 = "aabc"


def same_frequency(str_1, str_2):
    counter_i = {}
    counter_j = {}

    if (len(str_1) != len(str_2)):
        return False

    for i in str_1:
        print(i)
        counter_i[i] = counter_i.get(i, 0) + 1

    for j in str_2:
        print(j)
        counter_j[j] = counter_j.get(j, 0) + 1

    print(counter_i, counter_j)
    return counter_i == counter_j


print(same_frequency(str_1, str_2))
