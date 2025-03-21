class HashMapChaining:
    """鏈式位址雜湊表"""

    def __init__(self):
        """建構子"""
        self.size = 0  # 鍵值對數量
        self.capacity = 4  # 雜湊表容量
        self.load_thres = 2.0 / 3.0  # 觸發擴容的負載因子閾值
        self.extend_ratio = 2  # 擴容倍數
        self.buckets = [[] for _ in range(self.capacity)]  # 桶陣列

    def hash_func(self, key: int) -> int:
        """雜湊函式"""
        return key % self.capacity

    def load_factor(self) -> float:
        """負載因子"""
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        """查詢操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 走訪桶，若找到 key ，則返回對應 val
        for pair in bucket:
            if pair.key == key:
                return pair.val
        # 若未找到 key ，則返回 None
        return None

    def put(self, key: int, val: str):
        """新增操作"""
        # 當負載因子超過閾值時，執行擴容
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 走訪桶，若遇到指定 key ，則更新對應 val 並返回
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        # 若無該 key ，則將鍵值對新增至尾部
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """刪除操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 走訪桶，從中刪除鍵值對
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        """擴容雜湊表"""
        # 暫存原雜湊表
        buckets = self.buckets
        # 初始化擴容後的新雜湊表
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # 將鍵值對從原雜湊表搬運至新雜湊表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        """列印雜湊表"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + " -> " + pair.val)
            print(res)
