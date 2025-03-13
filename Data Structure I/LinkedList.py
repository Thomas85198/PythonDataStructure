class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
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
    # Array 的最前面移除掉，指向下一個值

    def shift(self):
        if self.head is None:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.length = 0
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp

    # unshift 最前面加一個值
    def unshift(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            new_node = Node(value)
            self.head = new_node
            self.head.next = temp
        self.length += 1

    # insert_at()
    def insert_at(self, index, value):
        if index > self.length - 1 or index < 0:
            return None
        elif index == 0:
            self.unshift(value)
            return
        elif index == self.length - 1:
            self.push(value)
            return
        current_node = self.head
        new_node = Node(value)
        # for loop index - 1 steps
        for i in range(1, index):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1
        return

    # remove_at()

    def print_all(self):
        if self.length == 0:
            print("Linked list is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next


my_linked_list = LinkedList()
my_linked_list.push("Mike")
my_linked_list.push("John")
my_linked_list.push("Smith")
my_linked_list.push("Anna")
# popped_value = my_linked_list.pop()
# print(popped_value.val)
my_linked_list.insert_at(2, "Miley")
# my_linked_list.shift()
my_linked_list.print_all()
print(my_linked_list.length)
