class Queue:
    def __init__(self):
        self.queue = [(None) for i in range(5)]
        self.rear = -1
        self.front = -1

    def isFull(self):
        return self.rear == len(self.queue) - 1

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def enQueue(self , element):
        if self.isFull():
            print('The Queue is full')
        elif self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = element
        else:
            self.rear += 1
            self.queue[self.rear] = element
    
    def deQueue(self):
        if self.isEmpty():
            print('The Queue is empty')
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.queue[self.front] = None
            self.front += 1

    def display(self):
        print(self.queue)


# Enqueue
q = Queue()
item = [i for i in range(5)]
for i in item:
    q.enQueue(i)

q.display()
# Check if the isFull() method works well
q.enQueue(20)

# Dequeue
for i in item:
    q.deQueue()
    if i == 3:
        break
    q.display()
