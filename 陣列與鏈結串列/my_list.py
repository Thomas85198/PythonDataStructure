class MyList:
    """串列類別"""

    def __init__(self):
        """建構子"""
        self._capacity: int = 10  # 串列容量
        self._arr: list[int] = [0] * self._capacity  # 陣列（儲存串列元素）
        self._size: int = 0  # 串列長度（當前元素數量）
        self._extend_ratio: int = 2  # 每次串列擴容的倍數

    def size(self) -> int:
        """獲取串列長度（當前元素數量）"""
        return self._size

    def capacity(self) -> int:
        """獲取串列容量"""
        return self._capacity

    def get(self, index: int) -> int:
        """訪問元素"""
        # 索引如果越界，則丟擲異常，下同
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]

    def set(self, num: int, index: int):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num: int):
        """在尾部新增元素"""
        # 元素數量超出容量時，觸發擴容機制
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        """在中間插入元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        # 元素數量超出容量時，觸發擴容機制
        if self._size == self.capacity():
            self.extend_capacity()
        # 將索引 index 以及之後的元素都向後移動一位
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        # 更新元素數量
        self._size += 1

    def remove(self, index: int) -> int:
        """刪除元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        # 將索引 index 之後的元素都向前移動一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        # 更新元素數量
        self._size -= 1
        # 返回被刪除的元素
        return num

    def extend_capacity(self):
        """串列擴容"""
        # 新建一個長度為原陣列 _extend_ratio 倍的新陣列，並將原陣列複製到新陣列
        self._arr = self._arr + [0] * \
            self.capacity() * (self._extend_ratio - 1)
        # 更新串列容量
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        """返回有效長度的串列"""
        return self._arr[: self._size]
