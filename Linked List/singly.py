class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            temp = temp.next 
            count += 1
        return count
    
    # Insertion
    def insertFirst(self,item):
        node = Node(item)
        node.next = self.head
        self.head = node
    
    def insertEnd(self,item):
        if self.isEmpty():
            self.insertFirst(item)
        else:
            node = Node(item)
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
    
    def insertAt(self,pos,item):
        length = self.length() + 1
        if pos < 1 or pos > length:
            print('Invalid position')
        elif pos == 1:
            self.insertFirst(item)
        elif pos == length+1:
            self.insertEnd(item)
        else:
            prev = pos - 1
            temp = self.head
            i = 1
            node = Node(item)
            while i < prev:
                temp = temp.next
                i += 1
            node.next = temp.next
            temp.next = node

    # Deletion
    def deleteFirst(self):
        if self.isEmpty():
            print('The Linked List is empty')
        else:
            temp = self.head
            self.head = temp.next
            del temp

    def deleteEnd(self):
        if self.isEmpty():
            print('The Linked List is empty')
        elif self.head.next == None:
            self.deleteFirst()
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next 
            target = temp.next 
            temp.next = None
            del target

    def deleteAt(self,pos):
        length = self.length()
        if pos < 1 or pos > length:
            print('Invalid position')
        elif pos == 1:
            self.deleteFirst()
        elif pos == length:
            self.deleteEnd()
        else:
            prev = pos - 1
            temp = self.head
            i = 1
            while i < prev:
                temp = temp.next
                i += 1
            target = temp.next
            temp.next = target.next 
            del target

    def reverse(self):
        if self.isEmpty():
            print('The Linked List is empty')
        else:
            prev = None
            current = self.head
            nextnode = self.head
            while nextnode != None:
                nextnode = nextnode.next
                current.next = prev
                prev = current
                current = nextnode
            self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.item , end="->")
            temp = temp.next

sll = SLL()
# Checking insertFirst() method
for i in range(10):
    sll.insertFirst(i)
# # Checking insertEnd() method
for i in range(10):
    sll.insertEnd(i)
# # Checking deleteFirst() method
for i in range(10):
    sll.deleteFirst()
# # Checking deleteEnd() method
for i in range(5):
    sll.deleteEnd()
# Checking deleteAt() method
sll.deleteAt(3)
sll.deleteAt(1)
sll.deleteAt(3)
# Checkig insertAt() method
sll.insertAt(1,110)
sll.insertAt(2,111)
sll.insertAt(4,112)
sll.insertAt(3,113)

# Checking Reverse method
print('Before reversing:')
sll.display()
print('\nAfter reversing:')
sll.reverse()
sll.display()