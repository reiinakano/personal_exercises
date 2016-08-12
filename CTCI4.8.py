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

def sorted_array_to_BST(array):
    if not array:
        return None

    length = len(array)
    mid = length/2

    root = TreeNode(array[mid])
    root.left = sorted_array_to_BST(array[0:mid])
    root.right = sorted_array_to_BST(array[mid+1:length])

    return root

def get_all_paths_to_sum_from_this_node(root, target_sum, sum_so_far=0, path_so_far=""):
    path_so_far += str(root.value) +" "
    paths_found = []

    if sum_so_far + root.value == target_sum:
        paths_found.append(path_so_far)

    if root.left:
        paths_found += get_all_paths_to_sum_from_this_node(root.left, target_sum, sum_so_far + root.value, path_so_far)
    if root.right:
        paths_found += get_all_paths_to_sum_from_this_node(root.right, target_sum, sum_so_far + root.value, path_so_far)

    return paths_found

def get_all_paths_to_sum_from_tree(root, target_sum):
    q = deque([root])
    paths_found = []
    while q:
        current_node = q.popleft()
        paths_found += get_all_paths_to_sum_from_this_node(current_node, target_sum)

        if current_node.left: q.append(current_node.left)
        if current_node.right: q.append(current_node.right)
    return paths_found


if __name__ == "__main__":
    my_list = range(10000)
    BST = sorted_array_to_BST(my_list)
    print "BST built"
    print get_all_paths_to_sum_from_tree(BST, 8807)