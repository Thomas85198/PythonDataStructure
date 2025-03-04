class ArrayStack:
    """基於陣列實現的堆疊"""

    def __init__(self):
        """建構子"""
        self._stack: list[int] = []

    def size(self) -> int:
        """獲取堆疊的長度"""
        return len(self._stack)

    def is_empty(self) -> bool:
        """判斷堆疊是否為空"""
        return self.size() == 0

    def push(self, item: int):
        """入堆疊"""
        self._stack.append(item)

    def pop(self) -> int:
        """出堆疊"""
        if self.is_empty():
            raise IndexError("堆疊為空")
        return self._stack.pop()

    def peek(self) -> int:
        """訪問堆疊頂元素"""
        if self.is_empty():
            raise IndexError("堆疊為空")
        return self._stack[-1]

    def to_list(self) -> list[int]:
        """返回串列用於列印"""
        return self._stack
