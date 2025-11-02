class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class CQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None and self.rear == None
    
    def length(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.front
            count = 1
            while temp.next != self.front:
                temp = temp.next
                count += 1 
            return count

    def enQueue(self,item):
        node = Node(item)
        if self.isEmpty():
            self.front = node
            self.rear = node
            self.rear.next = self.front
        else:
            self.rear.next = node
            self.rear = node
            self.rear.next = self.front

    def deQueue(self):
        if self.isEmpty():
            print("The Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            temp = self.front
            self.front = temp.next
            self.rear.next = self.front

    def peek(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            print(self.front.item)

    def display(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            temp = self.front
            while temp.next != self.front:
                print(temp.item,end = "->")
                temp = temp.next 
            print(temp.item)

q = CQueue()
for i in range(100):
    q.enQueue(i)

for i in range(50):
    q.deQueue()
q.display()