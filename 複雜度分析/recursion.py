def recur(n: int) -> int:
    """遞迴"""
    if n == 1:
        return 1
    res = recur(n - 1)
