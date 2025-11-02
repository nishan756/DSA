class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self,item):
        node = Node(item)
        node.next = self.top
        self.top = node
    
    def pop(self):
        temp = self.top
        self.top = temp.next
        del temp
    
    def peek(self):
        if self.isEmpty():
            print("The Stack is empty")
        else:
            temp = self.top
            return print("Top item is:",temp.item)
    
    def display(self):
        if self.isEmpty():
            print("The Stack is empty")
        else:
            temp = self.top
            while temp.next != None:
                print(temp.item,end="->")
                temp = temp.next
            print(temp.item)
    
stack = Stack()
# Checking push() method
for i in range(10):
    stack.push(i)
# Checking pop() method
for i in range(5):
    stack.pop()
    stack.peek()
stack.display()