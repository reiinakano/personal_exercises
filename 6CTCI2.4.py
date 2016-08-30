class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, node):
        self.next = node

    def __repr__(self):
        a = self
        to_print = [a.value]
        while a.next:
            to_print.append(a.next.value)
            a = a.next
        return "Linked list (head->tail) " + str(to_print)


def partition_around_x(head, x):
    if not head:
        return None
    front = head
    back = head
    current = head.next
    while current:
        if current.value >= x:
            front = current
        else:
            front.next = current.next
            current.next = back
            back = current
        current = front.next
    return back


if __name__ == "__main__":
    a = LinkedListNode(9)
    a.next = LinkedListNode(2)
    a.next.next = LinkedListNode(3)
    a.next.next.next = LinkedListNode(1)
    a.next.next.next.next = LinkedListNode(7)
    a.next.next.next.next.next = LinkedListNode(5)
    a.next.next.next.next.next.next = LinkedListNode(6)
    print a
    b = partition_around_x(a, 4)
    print b