class ListNode:
    """鏈結串列節點類別"""

    def __init__(self, val: int):
        self.val: int = val  # 節點值
        self.next: ListNode | None = None  # 後繼節點引用


def function() -> int:
    """ 函式 """
    return 0


def constant(n: int):
    """ 常數階 """
    a = 0
    nums = [0] * 10000
    node = ListNode(0)

    for _ in range(n):
        c = 0
    for _ in range(n):
        function()


def linear(n: int):
    """ 線性階 """
    nums = [0] * n
    hmap = dict[int, str]()
    for i in range(n):
        hmap[i] = str(i)


def linear_recur(n: int):
    """ 線性階（遞迴實現）"""
    print(" 遞迴 n =", n)
    if n == 1:
        return
    linear_recur(n - 1)


def quadratic(n: int):
    """ 平方階 """
    num_matrix = [[0] * n for _ in range(n)]
