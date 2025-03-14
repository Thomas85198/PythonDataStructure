class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # 我們目前人在哪裡
            current_node = self.head
            # 當我們找到最後一個節點時
            while current_node.next is not None:
                # 她就會不斷的跳下一個點
                current_node = current_node.next
            # 找到 Node 的最後一個節點，將新截點接上去
            current_node.next = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.length = 0
            return temp
        else:
            current_node = self.head
            for i in range(1, self.length - 1):
                current_node = current_node.next
            temp = current_node.next
            current_node.next = None
            self.length -= 1
            return temp

    def print_all(self):
        if self.length == 0:
            print("Linked list is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next


my_stack = Stack()
my_stack.push("Mike")
my_stack.push("John")
my_stack.push("Smith")
my_stack.push("Anna")

my_stack.print_all()
