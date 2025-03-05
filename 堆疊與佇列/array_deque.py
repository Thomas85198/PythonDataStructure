class ArrayDeque:
    """基於環形陣列實現的雙向佇列"""

    def __init__(self, capacity: int):
        """建構子"""
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        """獲取雙向佇列的容量"""
        return len(self._nums)

    def size(self) -> int:
        """獲取雙向佇列的長度"""
        return self._size

    def is_empty(self) -> bool:
        """判斷雙向佇列是否為空"""
        return self._size == 0

    def index(self, i: int) -> int:
        """計算環形陣列索引"""
        # 透過取餘操作實現陣列首尾相連
        # 當 i 越過陣列尾部後，回到頭部
        # 當 i 越過陣列頭部後，回到尾部
        return (i + self.capacity()) % self.capacity()

    def push_first(self, num: int):
        """佇列首入列"""
        if self._size == self.capacity():
            print("雙向佇列已滿")
            return
        # 佇列首指標向左移動一位
        # 透過取餘操作實現 front 越過陣列頭部後回到尾部
        self._front = self.index(self._front - 1)
        # 將 num 新增至佇列首
        self._nums[self._front] = num
        self._size += 1

    def push_last(self, num: int):
        """佇列尾入列"""
        if self._size == self.capacity():
            print("雙向佇列已滿")
            return
        # 計算佇列尾指標，指向佇列尾索引 + 1
        rear = self.index(self._front + self._size)
        # 將 num 新增至佇列尾
        self._nums[rear] = num
        self._size += 1

    def pop_first(self) -> int:
        """佇列首出列"""
        num = self.peek_first()
        # 佇列首指標向後移動一位
        self._front = self.index(self._front + 1)
        self._size -= 1
        return num

    def pop_last(self) -> int:
        """佇列尾出列"""
        num = self.peek_last()
        self._size -= 1
        return num

    def peek_first(self) -> int:
        """訪問佇列首元素"""
        if self.is_empty():
            raise IndexError("雙向佇列為空")
        return self._nums[self._front]

    def peek_last(self) -> int:
        """訪問佇列尾元素"""
        if self.is_empty():
            raise IndexError("雙向佇列為空")
        # 計算尾元素索引
        last = self.index(self._front + self._size - 1)
        return self._nums[last]

    def to_array(self) -> list[int]:
        """返回陣列用於列印"""
        # 僅轉換有效長度範圍內的串列元素
        res = []
        for i in range(self._size):
            res.append(self._nums[self.index(self._front + i)])
        return res
