class ListNode:
    """ 鏈結串列節點類別 """

    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


class LinkedListStack:
    """基於鏈結串列實現的堆疊"""

    def __init__(self):
        """建構子"""
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        """獲取堆疊的長度"""
        return self._size

    def is_empty(self) -> bool:
        """判斷堆疊是否為空"""
        return self._size == 0

    def push(self, val: int):
        """入堆疊"""
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        """出堆疊"""
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        """訪問堆疊頂元素"""
        if self.is_empty():
            raise IndexError("堆疊為空")
        return self._peek.val

    def to_list(self) -> list[int]:
        """轉化為串列用於列印"""
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr
