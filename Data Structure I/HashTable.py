class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # 初始化為空列表的列表

    # parse string to integer
    def parse(self, str):
        result = 0
        for i in range(len(str)):
            result += ord(str[i])
        return result

    # hash method for any key type
    def hash(self, key):
        if type(key) is not int:
            key_value = self.parse(key)
        else:
            key_value = key
        return key_value % self.size

    def set(self, key, value):
        index = self.hash(key)  # 使用通用的雜湊函數

        # 檢查是否已存在相同鍵的項目
        for i, item in enumerate(self.table[index]):
            if key in item:
                self.table[index][i] = {key: value}  # 更新值
                return

        # 如果不存在，添加新項目
        self.table[index].append({key: value})

    def get(self, key):
        index = self.hash(key)  # 使用通用的雜湊函數

        for item in self.table[index]:
            if key in item:
                return item[key]

        return None  # 未找到鍵

    def print_all(self):
        for i, bucket in enumerate(self.table):
            if bucket:  # 只打印非空的桶
                print(f"索引 {i}: {bucket}")


my_hash_table = HashTable(6)
my_hash_table.set("white", "#FFFFFF")
my_hash_table.set("black", "#000000")
my_hash_table.set("red", "#FF0000")
my_hash_table.set("blue", "#0000FF")
my_hash_table.set("magenta", "#FF00FF")

my_hash_table.print_all()
