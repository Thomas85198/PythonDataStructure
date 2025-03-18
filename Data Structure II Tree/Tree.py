class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def tree_insert(self, z):
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right

        if y is None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z


bst = BinarySearchTree()
bst.tree_insert(Node(15))
bst.tree_insert(Node(6))
bst.tree_insert(Node(5))
bst.tree_insert(Node(1))
bst.tree_insert(Node(13))
bst.tree_insert(Node(-7))
bst.tree_insert(Node(3))

print(bst.root.value)
