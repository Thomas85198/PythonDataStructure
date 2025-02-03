str_1 = "tacocat"
str_2 = "amanaplanacanalpanama"
str_3 = "asdfsafeaw"


def palindrome(str):
    # return str == str[::-1]
    left = 0
    right = len(str) - 1

    while (left <= right):
        if (str[left] == str[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


print(palindrome(str_1))
print(palindrome(str_2))
print(palindrome(str_3))
