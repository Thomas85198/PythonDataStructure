class Pair:
    """鍵值對"""

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val


class ArrayHashMap:
    """基於陣列實現的雜湊表"""

    def __init__(self):
        """建構子"""
        # 初始化陣列，包含 100 個桶
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        """雜湊函式"""
        index = key % 100
        return index

    def get(self, key: int) -> str:
        """查詢操作"""
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str):
        """新增操作"""
        pair = Pair(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        """刪除操作"""
        index: int = self.hash_func(key)
        # 置為 None ，代表刪除
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        """獲取所有鍵值對"""
        result: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self) -> list[int]:
        """獲取所有鍵"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self) -> list[str]:
        """獲取所有值"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result

    def print(self):
        """列印雜湊表"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)
