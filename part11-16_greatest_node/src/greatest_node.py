# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
def greatest_node(root: Node):
    greatest = root.value

    if root.left_child is not None:
        if greatest < greatest_node(root.left_child):
            greatest = greatest_node(root.left_child)

    if root.right_child is not None:
        if greatest < greatest_node(root.right_child):
            greatest = greatest_node(root.right_child)

    return greatest

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))

    tree2 = Node(3)

    tree2.left_child = Node(5)
    tree2.left_child.left_child = Node(7)
    tree2.left_child.right_child = Node(10)

    tree2.right_child = Node(3)
    tree2.right_child.left_child = Node(13)
    tree2.right_child.left_child.left_child = Node(6)
    tree2.right_child.right_child = Node(11)

    print(greatest_node(tree2))

        # determine if root, left child or right child is the greatest
    # if root.left_child is not None and root.right_child is not None:
    #     greatest = max(root.value, root.left_child.value, root.right_child.value)
    # elif root.left_child is None:
    #     if root.right_child is None:
    #         greatest = root.value
    #     else:
    #         greatest = max(root.value, root.right_child.value)
    # elif root.right_child is None:
    #     greatest = max(root.value, root.left_child.value)

    # if root.left_child is not None:
    #     greatest = greatest_node(root.left_child)
    
    # if root.right_child is not None:
    #     greatest = greatest_node(root.right_child)
    
    # return greatest

    # Solution
    # def greatest_node(root: Node):
    # value = root.value
 
    # if root.left_child:
    #     left_value = greatest_node(root.left_child)
    # else:
    #     left_value = value
 
    # if root.right_child:
    #     right_value = greatest_node(root.right_child)
    # else:
    #     right_value = value
 
    # return max(value, left_value, right_value)