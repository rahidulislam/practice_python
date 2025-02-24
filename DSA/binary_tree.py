class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self,root):
        if root:
            print(root.value, end="->")
            self.preorder(root.left)
            self.preorder(root.right)



    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value, end="->")
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end="->")
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

tree = BinaryTree()
print("Preorder:")
tree.preorder(root)
print("\nInorder:")
tree.inorder(root)
print("\nPostorder:")
tree.postorder(root)
# Output: