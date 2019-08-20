# Creating Node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

"""
In Order traversal: 
left subtree (recursion)
root
right subtree (recursion)
"""
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)


"""
Pre Order traversal: 
root
left subtree (recursion)
right subtree (recursion)
"""
def pre_order_traversal(root):
    if root:
        print(root.value, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


"""
Post Order traversal: 
left subtree (recursion)
right subtree (recursion)
root
"""
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")



# Driver Code
root = Node(1 )
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In order Traversal")
in_order_traversal(root)

print("\nPre order Traversal")
pre_order_traversal(root)

print("\nPost order Traversal")
post_order_traversal(root)



"""
Ref: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""