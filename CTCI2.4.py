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
        return str(to_print)

def add_digits(head1, head2):
    current1, current2 = head1, head2
    result_head = None
    current_result = None
    remainder = 0
    while(current1 or current2):
        sum = 0
        if current1 and current2:
            sum = current1.value + current2.value + remainder
        elif current1:
            sum = current1.value + remainder
        elif current2:
            sum = current2.value + remainder
        else:
            sum = 0
        if sum >= 10:
            sum -= 10
            remainder = 1
        else:
            remainder = 0
        if not current_result:
            result_head = LinkedListNode(sum)
            current_result = result_head
        else:
            current_result.next = LinkedListNode(sum)
            current_result = current_result.next
        if current1: current1 = current1.next
        if current2: current2 = current2.next
    if remainder:
        current_result.next = LinkedListNode(1)
    return result_head

if __name__ == "__main__":
    a = LinkedListNode(9)
    a.next = LinkedListNode(9)
    a.next.next = LinkedListNode(9)
    a.next.next.next = LinkedListNode(9)
    b = LinkedListNode(9)
    b.next = LinkedListNode(9)
    b.next.next = LinkedListNode(9)
    print add_digits(a,b)