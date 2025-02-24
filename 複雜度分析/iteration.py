def for_loop(n: int) -> int:
    """for 迴圈"""
    res = 0
    for i in range(1, n + 1):
        res += 1
    return res


def while_loop(n: int) -> int:
    """while 迴圈"""
    res = 0
    i = 1
    while i <= n:
        res += 1
        i += 1
    return res


def while_loop_ii(n: int) -> int:
    """while 迴圈 (兩次更新)"""
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res


def nested_for_loop(n: int) -> str:
    """雙層 for 迴圈"""
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i}, {j})"
    return res
