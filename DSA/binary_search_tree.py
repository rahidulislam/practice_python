class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root,key)

    def _insert(self,node,key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left,key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right,key)

    def search(self,key):
        return self._search(self.root,key)
    
    def _search(self,node,key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left,key)
        return self._search(node.right,key)
    
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

node = bst.search(7)
if node:
    print(f"Node found: {node.value}")
else:
    print("Node not found")
