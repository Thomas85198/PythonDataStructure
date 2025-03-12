class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.next: None


class LinkedList:
    def __init__(self):
        self.head: None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
