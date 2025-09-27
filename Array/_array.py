class Array:
    def __init__(self,size):
        self.array = [None]*size
        self.max_index = size - 1 #Max index of this array
        self.passed_index = -1 #Index of the last element
    
    def isFull(self):
        return self.passed_index == self.max_index
    
    def isEmpty(self):
        return self.passed_index == -1
    
    # Insertion methods
    def insertFirst(self,element):
        if self.isFull():
            print('The Array is full')
        else:
            for i in range(self.passed_index , -1 , -1):
                self.array[i+1] = self.array[i]
            self.array[0] = element
            self.passed_index += 1
    
    def insertEnd(self,element):
        if self.isFull():
            print('The Array is full')
        else:
            self.passed_index += 1
            self.array[self.passed_index] = element
    
    def insertAt(self,position,element):
        if self.isFull():
            print('The Array is full')
        elif position - 1 < 0 or position - 1 > self.passed_index:
            print('Invalid index')
        else:
            for i in range(self.passed_index , position - 2 , -1):
                self.array[i+1] = self.array[i]
            self.array[position - 1] = element
            self.passed_index += 1
    
    # Deletion methods
    def clean(self):
        if self.isEmpty():
            print('The Array is empty')
        else:
            self.array = [None]*(self.max_index+1)
            self.passed_index = -1
    
    def deleteFront(self):
        if self.isEmpty():
            print('The Array is empty')
        else:
            for i in range(0 , self.passed_index):
                self.array[i] = self.array[i +1]
            self.array[self.passed_index] = None
            self.passed_index -= 1
    
    def deleteEnd(self):
        if self.isEmpty():
            print('The Array is empty')
        else:
            self.array[self.passed_index] = None
            self.passed_index -= 1
    
    def deleteFrom(self,position):
        if self.isEmpty():
            print('The Array is empty')
        else:
            for i in range(position - 1 , self.passed_index):
                self.array[i] = self.array[i+1]
            self.array[self.passed_index] = None
            self.passed_index -= 1

    
    def display(self):
        print('Array:',self.array[:self.passed_index+1])
    
a = Array(20)

# Checking, if the insertFirst() method works properly
for i in range(10):
    a.insertFirst(i)
a.display()

# Checking, if the insertEnd() method works properly
for i in range(11 , 20):
    a.insertEnd(i)
a.display()

# Checking, if the inserAt() method works properly
a.insertAt(3 , 150)
a.display()

# Checking, if the deleteFront() method works properly
a.deleteFront()
a.display()

# Checking, if the deleteEnd() method works properly
a.deleteEnd()
a.display()

# Checking, if the deleteFromt() method works properly
a.deleteFrom(10)
a.display()

# Checking, if the clean() method works properly
a.clean()
a.display()
