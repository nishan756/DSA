class Node:
    def __init__(self,item):
        self.item = item
        self.prev = None
        self.next = None

class DeQueue:
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
            while temp.next != self.front:
                temp = temp.next 
                count += 1
            return count
    
    def enQueueFront(self , item):
        node = Node(item)
        if self.isEmpty():
            self.front = node
            self.rear = node

            self.front.prev = self.rear
            self.rear.next = self.front
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
            self.front.prev = self.rear
            self.rear.next = self.front
    
    def enQueueRear(self , item):
        node = Node(item)
        if self.isEmpty():
            self.front = node
            self.rear = node

            self.front.prev = self.rear
            self.rear.next = self.front
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
            self.rear.next = self.front
            self.front.prev = self.rear

    def deQueueFront(self):
        if self.isEmpty():
            print("The Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            temp = self.front
            temp.next.prev = self.rear
            self.front = temp.next
            self.rear.next = self.front
            del temp
    
    def deQueueRear(self):
        if self.isEmpty():
            print("The Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            temp = self.rear
            self.rear = temp.prev
            self.rear.next = self.front
            self.front.prev = self.rear
            del temp

    def forDisplay(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            temp = self.front
            while temp.next != self.front:
                print(temp.item,end="<->")
                temp = temp.next
            print(temp.item)
    
    def backDisplay(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            temp = self.rear
            while temp.prev != self.rear:
                print(temp.item,end="<->")
                temp = temp.prev
            print(temp.item)

q = DeQueue()
for i in range(10):
    q.enQueueFront(i)

for i in range(10):
    q.enQueueRear(i)

for i in range(5):
    q.deQueueRear()

for i in range(5):
    q.deQueueFront()
q.forDisplay()
print(f"Front:{q.front.item}\nPrev of Front:{q.front.prev.item}\nRear:{q.rear.item}\nNext of Rear:{q.rear.next.item}")