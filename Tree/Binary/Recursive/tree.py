class Node:
    def __init__(self , item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root is None
    
    def insert(self):
        item = int(input("Enter node item (0 for None):"))
        if item == 0:
            return 
        node = Node(item)

        print(f'Enter left child of {node.item}:')
        node.left = self.insert()

        print(f'Enter right child of {node.item}:')
        node.right = self.insert()

        return node

    def inOrder(self , root = None):
        if root is None:
            return 
        else:
            self.inOrder(root.left)
            print(root.item,end="->")
            self.inOrder(root.right)
    
    def preOrder(self , root = None):
        if root is None:
            return
        else:
            print(root.item,end="->")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self , root = None):
        if root is None:
            return
        else:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.item,end='->')

tree = BinaryTree()
tree.root = tree.insert()

print('\nInorder')
tree.inOrder(tree.root)

print('\nPreorder')
tree.preOrder(tree.root)

print('\nPostorder')
tree.postOrder(tree.root)
