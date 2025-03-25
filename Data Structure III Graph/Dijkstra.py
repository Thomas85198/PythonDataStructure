class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.edges = []
        self.distance_from_start_node = float('inf')
        self.previous = None

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


class MinHeap:
    def __init__(self):
        self.values = []

    def enqueue(self, node):
        # 檢查優先佇列是否為空
        if len(self.values) == 0:
            self.values.append(node)
            return True

        self.values.append(node)
        new_index = len(self.values) - 1
        parent_index = (new_index - 1) // 2

        while (parent_index >= 0 and
               self.values[new_index].distance_from_start_node <
               self.values[parent_index].distance_from_start_node):
            # 交換父節點和子節點
            self.values[parent_index], self.values[new_index] = self.values[new_index], self.values[parent_index]
            # 更新索引號
            new_index = parent_index
            parent_index = (new_index - 1) // 2

    def dequeue(self):
        if len(self.values) == 0:
            return None
        if len(self.values) == 1:
            removed_node = self.values.pop()
            return removed_node

        # 交換兩個節點
        temp = self.values.pop()
        self.values.append(self.values[0])
        self.values[0] = temp
        removed_node = self.values.pop()

        self.min_heapify(0)

        return removed_node

    def min_heapify(self, i):
        smallest = i
        l = i * 2 + 1
        r = i * 2 + 2

        if (l <= len(self.values) - 1 and
            self.values[l].distance_from_start_node <
                self.values[i].distance_from_start_node):
            smallest = l
        else:
            smallest = i

        if (r <= len(self.values) - 1 and
            self.values[r].distance_from_start_node <
                self.values[smallest].distance_from_start_node):
            smallest = r

        if smallest != i:
            # 交換
            self.values[i], self.values[smallest] = self.values[smallest], self.values[i]
            self.min_heapify(smallest)

    def decrease_priority(self, node):
        new_index = self.values.index(node)
        parent_index = (new_index - 1) // 2

        while (parent_index >= 0 and
               self.values[new_index].distance_from_start_node <
               self.values[parent_index].distance_from_start_node):
            # 交換節點和其父節點
            self.values[parent_index], self.values[new_index] = self.values[new_index], self.values[parent_index]
            # 更新索引號
            new_index = parent_index
            parent_index = (new_index - 1) // 2


def dijkstra(start_node):
    mh = MinHeap()
    start_node.distance_from_start_node = 0
    start_node.visited = True

    # 將所有節點加入最小堆
    mh.enqueue(A)
    mh.enqueue(B)
    mh.enqueue(C)
    mh.enqueue(D)
    mh.enqueue(E)
    mh.enqueue(F)

    current_node = mh.dequeue()

    while len(mh.values) > 0:
        # 1. 最小堆中的最小值節點 => current_node
        # 2. 遍歷 current_node 的鄰居中，沒有拜訪過的節點 => neighbor_node
        # 3. 如果 neighbor_node.distance > current_node.distance + weight
        # 4. 則更新 neighbor_node.distance = current_node.distance + weight
        # 5. 同時更新 neighbor_node.previous = current_node，並在最小堆中降低 neighbor_node 的優先級
        for edge in current_node.edges:
            neighbor_node = edge.node
            if not neighbor_node.visited:
                d1 = neighbor_node.distance_from_start_node
                d2 = current_node.distance_from_start_node
                d3 = edge.weight
                if d1 > d2 + d3:
                    neighbor_node.distance_from_start_node = d2 + d3
                    neighbor_node.previous = current_node
                    mh.decrease_priority(neighbor_node)

        current_node = mh.dequeue()
        current_node.visited = True


# 創建節點
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

# 添加邊
A.add_edge(Edge(B, 2))
A.add_edge(Edge(C, 2))
B.add_edge(Edge(A, 2))
B.add_edge(Edge(D, 1))
B.add_edge(Edge(E, 4))
C.add_edge(Edge(A, 2))
C.add_edge(Edge(D, 1))
C.add_edge(Edge(F, 2))
D.add_edge(Edge(B, 1))
D.add_edge(Edge(C, 1))
D.add_edge(Edge(E, 2))
D.add_edge(Edge(F, 3))
E.add_edge(Edge(B, 4))
E.add_edge(Edge(D, 2))
E.add_edge(Edge(F, 1))
F.add_edge(Edge(C, 2))
F.add_edge(Edge(D, 3))
F.add_edge(Edge(E, 1))

# 執行 Dijkstra 算法
dijkstra(A)

# 輸出結果
print("A 的資訊")
print(A.distance_from_start_node)
print(A.previous)

print("B 的資訊")
print(B.distance_from_start_node)
print(B.previous.value if B.previous else None)

print("C 的資訊")
print(C.distance_from_start_node)
print(C.previous.value if C.previous else None)

print("D 的資訊")
print(D.distance_from_start_node)
print(D.previous.value if D.previous else None)

print("E 的資訊")
print(E.distance_from_start_node)
print(E.previous.value if E.previous else None)

print("F 的資訊")
print(F.distance_from_start_node)
print(F.previous.value if F.previous else None)
