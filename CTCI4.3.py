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
    sorted_array_to_BST(my_list).inorder_traversal_with_height()