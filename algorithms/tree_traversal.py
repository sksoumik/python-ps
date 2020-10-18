# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# explanation: https://youtu.be/xo41NfT8218


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def print_preorder(root):
    if root:
        print(root.value, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.value, end=" ")
        print_in_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.value, end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal: ")
    print_preorder(root)

    print("\nInOrder traversal: ")
    print_in_order(root)

    print("\nPostOrder traversal: ")
    print_post_order(root)
    print()
