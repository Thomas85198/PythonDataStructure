class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, n):
        self.neighbors.append(n)


# 創建節點
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")
K = Node("K")
L = Node("L")
M = Node("M")

# 建立鄰接關係
A.add_neighbor(E)
A.add_neighbor(F)
B.add_neighbor(D)
C.add_neighbor(D)
D.add_neighbor(B)
D.add_neighbor(C)
D.add_neighbor(E)
D.add_neighbor(I)
E.add_neighbor(A)
E.add_neighbor(D)
E.add_neighbor(F)
E.add_neighbor(I)
F.add_neighbor(A)
F.add_neighbor(E)
F.add_neighbor(I)
G.add_neighbor(H)
G.add_neighbor(I)
H.add_neighbor(G)
H.add_neighbor(I)
H.add_neighbor(L)
I.add_neighbor(D)
I.add_neighbor(E)
I.add_neighbor(F)
I.add_neighbor(G)
I.add_neighbor(H)
I.add_neighbor(J)
I.add_neighbor(K)
I.add_neighbor(M)
J.add_neighbor(I)
J.add_neighbor(M)
K.add_neighbor(I)
K.add_neighbor(L)
K.add_neighbor(M)
L.add_neighbor(H)
L.add_neighbor(K)
M.add_neighbor(I)
M.add_neighbor(J)
M.add_neighbor(K)

# 深度優先遍歷


def DFT(starter):
    result = []

    def dft_helper(node):
        node.visited = True
        result.append(node.value)
        for neighbor in node.neighbors:
            if not neighbor.visited:
                dft_helper(neighbor)

    dft_helper(starter)
    return result

# 廣度優先遍歷


def BFT(starter):
    result = []
    queue = []

    queue.append(starter)
    starter.visited = True

    while len(queue) != 0:
        first_node = queue.pop(0)
        result.append(first_node.value)

        for neighbor in first_node.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)

    return result


# 重設所有節點為未訪問狀態（在運行 BFT 前）
for node in [A, B, C, D, E, F, G, H, I, J, K, L, M]:
    node.visited = False

print(*BFT(F))
