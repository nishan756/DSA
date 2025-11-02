class Stack:
    def __init__(self,size):
        self.max_index = size - 1
        self.stack = [None]*size
        self.top = -1
    
    def isFull(self):
        return self.top == self.max_index

    def isEmpty(self):
        return self.top == -1

    def push(self,item):
        if self.isFull():
            print('The Stack is full')
        else:
            self.top += 1
            self.stack[self.top] = item
    
    def pop(self):
        if self.isEmpty():
            print('The Stack is empty')
        else:
            self.stack[self.top] = None
            self.top -= 1
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[self.top]
        
    def display(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print('Stack:',self.stack[0:self.top+1])

s = Stack(20)

# Chesking push method
for i in range(20):
    s.push(i)

# Chesking pop method
for i in range(15):
    s.pop()

# Checking display method
s.display()
print(s.top)