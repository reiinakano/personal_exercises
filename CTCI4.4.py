from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder_traversal(self):
        if self.left: self.left.inorder_traversal()
        print self.value
        if self.right: self.right.inorder_traversal()

    def inorder_traversal_with_height(self, current_height=0):
        if self.left: self.left.inorder_traversal_with_height(current_height + 1)
        print str(self.value) + " at depth " + str(current_height)
        if self.right: self.right.inorder_traversal_with_height(current_height + 1)

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

def linked_list_from_BST(root):
    list_of_linked_lists = []
    q = deque([(root, 0)])
    previous_depth = -1
    current_head = None
    while q:
        current = q.popleft()
        current_node = current[0]
        print "Current node: " + str(current_node.value)
        current_depth = current[1]
        print "Current depth: " + str(current_depth)

        if current_node.left: q.append((current_node.left, current_depth+1))
        if current_node.right: q.append((current_node.right, current_depth+1))

        if current_depth != previous_depth:
            print "Generating new linked list\n"
            current_head = LinkedListNode(current_node.value)
            list_of_linked_lists.append(current_head)
        else:
            print "Appending a new node to current linked list\n"
            current_head.next = LinkedListNode(current_node.value)
            current_head = current_head.next

        previous_depth = current_depth

    return list_of_linked_lists

def sorted_array_to_BST(array):
    if not array:
        return None

    length = len(array)
    mid = length/2

    root = TreeNode(array[mid])
    root.left = sorted_array_to_BST(array[0:mid])
    root.right = sorted_array_to_BST(array[mid+1:length])

    return root


if __name__ == "__main__":
    my_list = range(1000)
    BST = sorted_array_to_BST(my_list)
    mylistoflinkedlist = linked_list_from_BST(BST)
    for i in mylistoflinkedlist:
        print i
        print " "
