class CQueue:
    def __init__(self,size:int):
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size
    
    def isFull(self):
        return (self.rear+1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enQueue(self,element):
        if self.isFull():
            print("The Queue is full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = element
    
    def deQueue(self):
        if self.isEmpty():
            print("The Queue is empty")
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
    
    def display(self):
        if self.front == -1:
            print("The Queue is full")
        
        i = self.front
        elements = []
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = ( i+1 ) % self.size
        print(elements)


q = CQueue(5)
LIST = ["Junayed","Ratri","Nishan",'Raozan','Pilot Shakib']

print('Enqueue')
for i in LIST:
    q.enQueue(i)
    print('Front:',q.front,'Rear:',q.rear)
q.display()

print("Dequeue")
for i in range(3):
    q.deQueue()
    q.enQueue(i)
    print('Front:',q.front,'Rear:',q.rear)
q.display()

