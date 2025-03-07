def unique_letter_substring(str):
    counter = {}
    left = 0
    right = 0
    max_length = 0  # 改為 0 而非 float('-inf')

    while right < len(str):
        # 如果右指針的字符已經在窗口中
        if str[right] in counter and counter[str[right]] > 0:
            # 應該減少當前右指針指向的重複字符的計數
            # 而不是左指針指向的字符
            counter[str[right]] -= 1
            # 或者更好的做法是移動左指針直到排除重複字符
            while left < right and str[left] != str[right]:
                if str[left] in counter:
                    counter[str[left]] -= 1
                left += 1
            # 跳過造成重複的字符
            if left < right and str[left] == str[right]:
                left += 1
        else:
            counter[str[right]] = 1
            right += 1
            max_length = max(max_length, right - left)

    print(max_length)
    return max_length


unique_letter_substring('thisishowwedoit')
