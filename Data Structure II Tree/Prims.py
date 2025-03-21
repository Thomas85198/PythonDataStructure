class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.edges = []

    def add_neighbor(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


# 創建節點
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
all_nodes = [A, B, C, D, E, F]

# 創建邊並添加到相應的節點
e1 = Edge(A, B, 10)
A.add_neighbor(e1)
B.add_neighbor(e1)

e2 = Edge(A, C, 8)
A.add_neighbor(e2)
C.add_neighbor(e2)

e3 = Edge(B, D, 6)
B.add_neighbor(e3)
D.add_neighbor(e3)

e4 = Edge(C, D, 5)
C.add_neighbor(e4)
D.add_neighbor(e4)

e5 = Edge(B, E, 7)
B.add_neighbor(e5)
E.add_neighbor(e5)

e6 = Edge(D, E, 4)
D.add_neighbor(e6)
E.add_neighbor(e6)

e7 = Edge(D, F, 3)
D.add_neighbor(e7)
F.add_neighbor(e7)

e8 = Edge(E, F, 1)
E.add_neighbor(e8)
F.add_neighbor(e8)

e9 = Edge(C, F, 8)
C.add_neighbor(e9)
F.add_neighbor(e9)


def get_best_edge(bucket):
    """找到權重最小且連接一個已訪問和一個未訪問節點的邊"""
    best_edge = None

    while best_edge is None and len(bucket) != 0:
        # 找出權重最小的邊
        best_edge = bucket[0]
        index = 0

        for i, edge in enumerate(bucket):
            if edge.weight < best_edge.weight:
                best_edge = edge
                index = i

        # 如果這條邊的兩個節點都已經訪問過，則不要這條邊
        if best_edge.node1.visited and best_edge.node2.visited:
            bucket.pop(index)
            best_edge = None

    return best_edge


def mst_prim(start_node):
    """使用 Prim 算法計算最小生成樹"""
    bucket = []
    mst_edges = []

    # 把起始節點標記為已訪問
    start_node.visited = True

    # 把起始節點的所有邊加入到候選集合
    for edge in start_node.edges:
        bucket.append(edge)

    best_edge = get_best_edge(bucket)

    while best_edge is not None:
        n1 = best_edge.node1
        n2 = best_edge.node2

        # 標記兩個節點為已訪問
        n1.visited = True
        n2.visited = True

        # 添加到最小生成樹
        mst_edges.append(best_edge)

        # 重置候選邊集合
        bucket = []

        # 對於所有已訪問的節點，將其未包含在MST中的邊加入候選集
        for node in all_nodes:
            if node.visited:
                for edge in node.edges:
                    if edge not in mst_edges:
                        bucket.append(edge)

        best_edge = get_best_edge(bucket)

    return mst_edges


# 執行算法
result = mst_prim(A)

# 輸出結果
print("最小生成樹的邊:")
for edge in result:
    print(f"{edge.node1.value} -- {edge.node2.value}: {edge.weight}")
