# print all the full nodes in a binary tree.
# https://www.geeksforgeeks.org/print-full-nodes-binary-tree/


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def full_nodes(root):
    if root:
        full_nodes(root.left)
        if (root.left != None) and (root.right != None):
            print(root.value, end=" ")
        full_nodes(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(7)

    full_nodes(root)
    print()
