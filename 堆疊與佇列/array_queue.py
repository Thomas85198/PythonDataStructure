class ArrayQueue:
    """基於環形陣列實現的佇列"""

    def __init__(self, size: int):
        """建構子"""
        self._nums: list[int] = [0] * size  # 用於儲存佇列元素的陣列
        self._front: int = 0  # 佇列首指標，指向佇列首元素
        self._size: int = 0  # 佇列長度

    def capacity(self) -> int:
        """獲取佇列的容量"""
        return len(self._nums)

    def size(self) -> int:
        """獲取佇列的長度"""
        return self._size

    def is_empty(self) -> bool:
        """判斷佇列是否為空"""
        return self._size == 0

    def push(self, num: int):
        """入列"""
        if self._size == self.capacity():
            raise IndexError("佇列已滿")
        # 計算佇列尾指標，指向佇列尾索引 + 1
        # 透過取餘操作實現 rear 越過陣列尾部後回到頭部
        rear: int = (self._front + self._size) % self.capacity()
        # 將 num 新增至佇列尾
        self._nums[rear] = num
        self._size += 1

    def pop(self) -> int:
        """出列"""
        num: int = self.peek()
        # 佇列首指標向後移動一位，若越過尾部，則返回到陣列頭部
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num

    def peek(self) -> int:
        """訪問佇列首元素"""
        if self.is_empty():
            raise IndexError("佇列為空")
        return self._nums[self._front]

    def to_list(self) -> list[int]:
        """返回串列用於列印"""
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._nums[(j % self.capacity())]
            j += 1
        return res
