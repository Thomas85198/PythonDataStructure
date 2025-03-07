def rs(n):
    print(f'我們方法有幾個 rs{n}')
    if n == 1:
        return 10
    else:
        return rs(n - 1) + 15


print(rs(3))

"""
rs(3) => 25 + 15 = 40
rs(2) => 10 + 15 = 25
rs(1) => 10
"""
