class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
    
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

    def lastnode(self):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        return temp
    
    # InsertFirst
    def insertFirst(self,item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            node.next = self.head
        else:
            lastnode = self.lastnode()
            lastnode.next = node
            node.next = self.head
            self.head = node
    
    def insertEnd(self,item):
        if self.isEmpty():
            self.insertFirst(item)
        else:
            node = Node(item)
            lastnode = self.lastnode()
            lastnode.next = node
            node.next = self.head
    
    def insertAt(self,pos,item):
        length = self.length()
        if pos < 1 or pos > length:
            print('Invalid position')
        elif pos == 1:
            self.insertFirst(item)
        else:
            temp = self.head
            node = Node(item)
            i = 1
            while i < pos - 1:
                temp = temp.next
                i += 1
                if temp.next == self.head:
                    break
            target = temp.next
            temp.next = node
            node.next = target

    # Deletion
    def deleteFirst(self):
        if self.isEmpty():
            print('The Linked List is empty')
        elif self.length() == 1:
            temp = self.head
            self.head = None
            del temp
        else:
            temp = self.head
            nextnode = temp.next
            lastnode = self.lastnode()
            self.head = nextnode
            lastnode.next = self.head
            del temp
    
    def deleteEnd(self):
        if self.isEmpty():
            print('The Linked List is empty')
        elif self.length() == 1:
            self.deleteFirst()
        else:
            temp = self.head
            lastnode = self.lastnode()
            prev = self.length() - 1
            i = 1
            while i < prev:
                temp = temp.next
                i += 1
            temp.next = self.head
            del lastnode

    def deleteAt(self,pos):
        length = self.length()
        if self.isEmpty():
            print('The Linked List is empty')
        elif pos < 1 or pos > length:
            print('Invalid position')
        elif pos == 1:
            self.deleteFirst()
        elif pos == length:
            self.deleteEnd()
        else:
            pos = pos - 1
            i = 1
            prev = self.head
            while i < pos:
                prev = prev.next
                i += 1
            target = prev.next
            nextnode = target.next 
            prev.next = nextnode
            del target
        
    def display(self):
        if self.isEmpty():
            print('The Linked List is empty')
        temp = self.head
        while temp:
            print(temp.item,end="->")
            temp = temp.next
            if temp == self.head:
                break
    

sll = Circular()

# Checking insertFirst() method
for i in range(10):
    sll.insertFirst(i)

# Checking insertAt() method
sll.insertAt(1,110)
sll.insertAt(11,111)
sll.insertAt(12,113)

# Checking deleteFirst() method
for i in range(13):
    sll.deleteFirst()

# Checking deleteEnd() method
for i in range(10):
    sll.deleteEnd()

# Checking deleteAt() method
sll.deleteAt(5)
sll.deleteAt(1)
sll.deleteAt(11)
sll.deleteAt(10)
# Checking display() method
sll.display()
            




