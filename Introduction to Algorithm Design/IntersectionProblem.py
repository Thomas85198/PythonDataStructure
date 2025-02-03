arr_1 = [15, 3, 6, 8, 24, 16]
arr_2 = [11, 3, 9, 6, 15, 8]
intersection_arr = list(set(arr_1) & set(arr_2))

# O(n) 如果用 lambda 或是 comprehension 會比較慢 O(n^2)
print(intersection_arr)
