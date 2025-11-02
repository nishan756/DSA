class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    def length(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.front
            count = 1
            while temp.next != None:
                temp = temp.next
                count += 1
            return count
    
    def enQueue(self,item):
        node = Node(item)
        if self.isEmpty():
            self.front = node 
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deQueue(self):
        if self.isEmpty():
            print("The Queue is empty")
        elif self.front.next == None:
            temp = self.front
            self.front = None
            self.rear = None
            del temp
        else:
            temp = self.front
            self.front = temp.next
            del temp
    
    def peek(self):
        if self.isEmpty():
            print("None")
        else:
            print(self.front.item)
    
    def display(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            temp = self.front
            while temp.next != None:
                print(temp.item,end="->")
                temp = temp.next
            print(temp.item)

queue = Queue()
for i in range(10):
    queue.enQueue(i)
for i in range(5):
    queue.deQueue()
queue.display()
print(queue.length())
