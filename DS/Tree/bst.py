class Node:
    def __init__(self , item):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self , root , item):
        if root is None:
            return Node(item)
        if item < root.item:
            root.left = self.insert(root.left , item)
        if item > root.item:
            root.right = self.insert(root.right , item)
        return root
    
    def search(self , root , item):
        if root is None:
            return 'Not found'
        if root.item == item:
            return 'Found'
        if item < root.item:
            return self.search(root.left , item)
        if item > root.item:
            return self.search(root.right , item)
    
    
    
    def inOrder(self , root):
        if root is None:
            return None
        else:
            self.inOrder(root.left)
            print(root.item,end="->")
            self.inOrder(root.right)
    
    def preOrder(self , root):
        if root is None:
            return None
        else:
            print(root.item,end="->")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self , root):
        if root is None:
            return None
        else:
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(root.item,end="->")

bst = BST()
bst.root = bst.insert(bst.root , 20)

for i in range(10):
    bst.insert(bst.root,i)

print('\nInorder')
bst.inOrder(bst.root)

print('\nPreorder')
bst.preOrder(bst.root)

print('\nPostorder')
bst.postOrder(bst.root)

# Searching
print(bst.search(bst.root , 10))
print(bst.search(bst.root , 8))
print(bst.search(bst.root , 7))
print(bst.search(bst.root , 12))

