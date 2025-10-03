class DeQueue:
    def __init__(self,size):
        self.max_index = size - 1
        self.front = -1
        self.rear = -1
        self.queue = [None]*size
    
    def isFull(self):
        return (self.front == 0 and self.rear == self.max_index) or self.front == self.rear + 1
    
    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    
    def enQueueFront(self , item):
        if self.isFull():
            print("The Queue is full")

        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.front] = item

        elif self.front == 0:
            self.front = self.max_index
            self.queue[self.front] = item
        else:
            self.front -= 1
            self.queue[self.front] = item
    
    def deQueueFront(self):
        if self.isEmpty():
            print("The Queue is empty")
        
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1

        elif self.front == self.max_index:
            self.queue[self.front] = None
            self.front = 0

        else:
            self.queue[self.front] = None
            self.front += 1
    
    def enQueueRear(self , item):
        if self.isFull():
            print('The Queue is full')

        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        
        elif self.rear == self.max_index:
            self.rear = 0
            self.queue[self.rear] = item
        
        else:
            self.rear += 1
            self.queue[self.rear] = item
    
    def deQueueRear(self):
        if self.isEmpty():
            print('The Queue is empty')
        
        elif self.front == self.rear:
            self.queue[self.rear] = None
            self.front = -1
            self.rear = -1
        
        elif self.rear == 0:
            self.queue[self.rear] = None
            self.rear = self.max_index
        
        else:
            self.queue[self.rear] = None
            self.rear -= 1
    
    def display(self):
        if self.front == -1:
            print("The Queue is empty")
        
        i = self.front
        elements = []
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = ( i+1 ) % (self.max_index+1)
        print(elements)

q = DeQueue(20)
for i in range(10):
    q.enQueueFront(i)
for i in range(10):
    q.enQueueRear(i)
for i in range(5):
    q.deQueueFront()
for i in range(5):
    q.deQueueRear()
q.display()
print(q.queue)