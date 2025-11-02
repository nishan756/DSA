class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.head
            count = 1
            while temp.next != self.head:
                temp = temp.next 
                count += 1
            return count
    
    # Insertion method
    def insertFirst(self,item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.tail.next = node

    def insertEnd(self,item):
        if self.isEmpty():
            self.insertFirst(item)
        else:
            node = Node(item)
            node.next = self.head
            self.tail.next = node
            self.tail = node

    def insertAt(self,pos,item):
        length = self.length()
        if pos < 1 or pos > length+1:
            print('Invalid position')
        elif pos == 1:
            self.insertFirst(item)
        elif pos == length+1:
            self.insertEnd(item)
        else:
            node = Node(item)
            temp = self.head
            i = 1
            while i < pos - 1:
                temp = temp.next
                i += 1
            target = temp.next
            node.next = target
            temp.next = node

    # Deletion meethods
    def deleteFirst(self):
        if self.isEmpty():
            print('The Linked List is empty')
        elif self.head.next == self.head:
            temp = self.head
            self.head = None 
            self.tail = None
            del temp
        else:
            temp = self.head
            self.tail.next = temp.next
            self.head = temp.next
            del temp
    
    def deleteEnd(self):
        if self.isEmpty() or self.head.next == self.head:
            self.deleteFirst()
        else:
            temp = self.head
            lastnode = self.tail
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            del lastnode

    def deleteAt(self,pos):
        length = self.length()
        if pos < 1 or pos > length:
            print('Invalid position')
        elif pos == 1:
            self.deleteFirst()
        elif pos == length:
            self.deleteEnd()
        else:
            pos = pos -1
            i = 1
            temp = self.head
            while i < pos:
                temp = temp.next
                i += 1
            target = temp.next
            temp.next = target.next 
            del target

    def display(self):
        if self.isEmpty():
            print('The Linked List is empty')
        else:
            temp = self.head 
            while temp.next != self.head:
                print(temp.item,end="->")
                temp = temp.next
            print(temp.item) 

sll = Circular()
# Checking insertFirst() method
for i in range(10):
    sll.insertFirst(i)

# Checking insertEnd() method
for i in range(20 , 11 , -1):
    sll.insertEnd(i)

# Checking insertAt() method
sll.insertAt(1,13)
sll.insertAt(20,14)
sll.insertAt(5,15)

# Checking deleteFirst() method
for i in range(5):
    sll.deleteFirst()

# Checking deleteEnd() method
for i in range(5):
    sll.deleteEnd()

# Checking deleteAt() method
sll.deleteAt(1)
sll.deleteAt(11)
sll.deleteAt(6)
# Checking display() method
sll.display()
print(f'\nHead:{sll.head.item}\nTail:{sll.tail.item}--Next-->{sll.tail.next.item}\nLength:{sll.length()}')