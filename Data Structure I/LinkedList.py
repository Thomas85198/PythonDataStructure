class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: None
        self.length = 0

    def push(value):
        new_node = Node(value)
