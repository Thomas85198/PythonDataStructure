str1 = "abbc"
str2 = "babc"


def same_frequency(str1, str2):
    if len(str1) != len(str2):
        return False
    counter1 = {}
    counter2 = {}

    for i in range(len(str1)):
        if str1[i] in counter1:
            counter1[str1[i]] += 1
        else:
            counter1[str1[i]] = 1

    for j in range(len(str2)):
        if str2[j] in counter2:
            counter2[str2[j]] += 1
        else:
            counter2[str2[j]] = 1

    print(counter1, counter2)

    for key, value in counter1.items():
        if key not in counter2:
            return False
        elif counter1[key] != counter2[key]:
            return False
        else:
            return True


print(same_frequency(str1, str2))
