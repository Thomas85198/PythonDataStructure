class ListNode:
    """ 鏈結串列節點類別 """

    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


def insert(n0: ListNode, P: ListNode):
    """ 在鏈結串列的節點 n0 之後插入節點 P """
    n1 = n0.next
    P.next = n1
    n0.next = P


def remove(n0: ListNode):
    """ 刪除鏈結串列的節點 n0 之後的首個節點 """
    if not n0.next:
        return
    P = n0.next
    n1 = P.next
    n0.next = n1


def access(head: ListNode, index: int) -> ListNode | None:
    """ 訪問鏈結串列中所引爲 index 的節點 """
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


def find(head: ListNode, target: int) -> int:
    """ 在鏈結串列中查詢值為 target 的首個節點 """
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1

    return -1
