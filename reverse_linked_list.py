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


def reverse_LL(head):
    current_node = None
    next_node = head

    while next_node:
        previous_node = current_node
        current_node = next_node
        next_node = current_node.next
        current_node.next = previous_node

    return current_node


if __name__ == "__main__":
    a = LinkedListNode(9)
    a.next = LinkedListNode(2)
    a.next.next = LinkedListNode(3)
    a.next.next.next = LinkedListNode(1)
    print a
    b = reverse_LL(a)
    print b