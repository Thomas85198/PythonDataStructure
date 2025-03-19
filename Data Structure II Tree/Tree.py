class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.path = ""
        self.queue = []

    def tree_insert(self, z):
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search_recursively(self, x, key):
        if x is None or key == x.key:
            return x
        elif key < x.key:
            return self.search_recursively(x.left, key)
        else:
            return self.search_recursively(x.right, key)

    def search_iteratively(self, x, key):
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right

        if x is None:
            print("Node not found")
        else:
            print("Node found.")
        return x

    def pre_order(self, n):
        if n is not None:
            self.path += str(n.key) + " "
            self.pre_order(n.left)
            self.pre_order(n.right)

    def in_order(self, n):
        if n is not None:
            self.in_order(n.left)
            self.path += str(n.key) + " "
            self.in_order(n.right)

    def post_order(self, n):
        if n is not None:
            self.post_order(n.left)
            self.post_order(n.right)
            self.path += str(n.key) + " "

    def bftt(self, n):
        if n is not None:
            self.queue.append(n)
            for i in range(len(self.queue)):
                current_node = self.queue[i]
                if current_node is not None:
                    if current_node.left is not None:
                        self.queue.append(current_node.left)
                    if current_node.right is not None:
                        self.queue.append(current_node.right)


# 使用範例
bst = BinarySearchTree()
bst.tree_insert(Node(15))
bst.tree_insert(Node(6))
bst.tree_insert(Node(5))
bst.tree_insert(Node(1))
bst.tree_insert(Node(13))
bst.tree_insert(Node(-7))
bst.tree_insert(Node(3))

result = bst.search_iteratively(bst.root, 15)
print(result.key)
