def recur(n: int) -> int:
    """遞迴"""
    if n == 1:
        return 1
    res = recur(n - 1)
    return n + res


def tail_recur(n, res):
    """ 尾遞迴 """
    if n == 0:
        return res
    return tail_recur(n - 1, res + n)


def fib(n: int) -> int:
    """ 費波那契數列：遞迴 """
    if n == 1 or n == 2:
        return n - 1
    res = fib(n - 1) + fib(n - 2)
    return res


def for_loop_recur(n: int) -> int:
    """ 使用跌代模擬遞迴 """
    stack = []
    res = 0
    for i in range(n, 0, -1):
        stack.append(i)
    while stack:
        res += stack.pop()
    return res
