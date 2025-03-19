class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        # 檢查 PriorityQueue 是否為空
        if len(self.values) == 0:
            self.values.append(new_node)
            return True
        self.values.append(new_node)
        new_index = len(self.values) - 1
        parent_index = (new_index - 1) // 2

        while parent_index >= 0 and self.values[new_index].priority > self.values[parent_index].priority:
            # swap parent and child
            self.values[new_index], self.values[parent_index] = self.values[parent_index], self.values[new_index]
            # update index
            new_index = parent_index
            parent_index = (new_index - 1) // 2

    def dequeue(self):
        if len(self.values) == 0:
            return None
        if len(self.values) == 1:
            removed_node = self.values.pop()
            return removed_node
        # swap two nodes
        temp = self.values.pop()
        self.values.append(self.values[0])
        self.values[0] = temp
        removed_node = self.values.pop()

        self.max_heapify(0)

        return removed_node

    def max_heapify(self, i):
        largest = i
        l = 2 * i + 1  # 左子節點索引
        r = 2 * i + 2  # 右子節點索引

        # 檢查左子節點是否存在且大於當前節點
        if l < len(self.values) and self.values[l].priority > self.values[i].priority:
            largest = l

        # 檢查右子節點是否存在且大於目前找到的最大節點
        if r < len(self.values) and self.values[r].priority > self.values[largest].priority:
            largest = r

        # 如果最大節點不是當前節點，則交換並遞迴調整堆
        if largest != i:
            # 交換節點
            self.values[i], self.values[largest] = self.values[largest], self.values[i]
            # 遞迴調整子樹
            self.max_heapify(largest)


pq = PriorityQueue()
pq.enqueue("Eat Breakfast", 5)
pq.enqueue("Learn Java", 2)
pq.enqueue("Learn Python", 7)
pq.enqueue("Buy Textbooks", 8)
pq.enqueue("Watch Neflix", 12)
pq.enqueue("Pay Bills", 15)

task = pq.dequeue()
task = pq.dequeue()


print(pq.values[0].value)  # "Learn Python"
print(task.value)  # Watch Netflix

while len(pq.values) >= 1:
    task = pq.dequeue()
    print(f"{task.value} , {task.priority}")
