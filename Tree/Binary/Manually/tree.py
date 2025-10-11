class Node:
    def __init__(self , item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self , root:Node):
        self.root = root
    
    def isEmpty(self):
        return self.root is None
    
    def insertLeft(self , current:Node , item:int):
        node = Node(item)
        if self.isEmpty():
            self.root = node
        elif current.left:
            node.left = current.left
            current.left = node
        else:
            current.left = node
    
    def insertRight(self , current:Node , item:int):
        node = Node(item)
        if self.isEmpty():
            self.root = node
        elif current.right:
            node.right = current.right
            current.right = node
        else:
            current.right = node
    
    def inOrder(self , root:Node):
        if root:
            self.inOrder(root.left)
            print(root.item,end="->")
            self.inOrder(root.right)

    def preOrder(self, root:Node):
        if root:
            print(root.item,end='->')
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self, root:Node):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.item,end='->')

root = Node(1)
tree = BinaryTree(root)
tree.insertLeft(root, 2)
tree.insertRight(root, 3)
tree.insertLeft(root.left, 4)
tree.insertRight(root.left, 5)

print('\nInorder Traversal')
tree.inOrder(root)

print('\nPreorder Traversal')
tree.preOrder(root)

print('\nPostorder Traversal')
tree.preOrder(root)


