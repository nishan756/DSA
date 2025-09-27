class Node:
    def __init__(self,item):
        self.item = item
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            temp = temp.next 
            count += 1
        return count
    
    def getHeadTail(self):
        print(f'\nHead:{self.head.item}\nTail:{self.tail.item}')

    # Insertion
    def insertFirst(self,item):
        node = Node(item)
        if self.isEmpty():
            self.head = node 
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insertEnd(self,item):
        if self.isEmpty():
            self.insertFirst(item)
        else:
            prev = self.tail
            node = Node(item)
            node.prev = prev
            prev.next = node
            self.tail = node
    
    def insertAt(self,pos,item):
        length = self.length()
        if pos < 1 or pos > length:
            print('Invalid Position')
        
        elif self.isEmpty() or pos == 1:
            self.insertFirst(item)

        elif pos == length:
            self.insertEnd(item)
        
        else:
            i = 1
            prev = pos - 1
            temp = self.head
            node = Node(item)
            while i < prev:
                temp = temp.next
                i += 1
            node.prev = temp
            node.next = temp.next
            temp.next = node
    
    # Deletion
    def deleteFirst(self):
        if self.isEmpty():
            print('The Linked list is empty')
        elif self.head.next == None:
            node = self.head
            self.head = None
            self.tail = None
            del node
        else:
            target = self.head
            next_node = target.next
            next_node.prev = None
            self.head = next_node
            del target
    
    def deleteEnd(self):
        if self.isEmpty():
            print('The Linked List is empty')
        elif self.tail.prev == None:
            self.deleteFirst()
        else:
            target = self.tail
            prev = target.prev
            prev.next = None
            self.tail = prev
            del target
    
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
            prev = self.head
            i = 1
            while i < pos:
                prev = prev.next 
                i += 1
            target = prev.next
            next_node = target.next 
            prev.next = next_node
            next_node.prev = prev
            del target

    def ForDisplay(self):
        node = self.head
        while node != None:
            print(node.item,end="<->")
            node = node.next
    
    def BackDisplay(self):
        node = self.tail
        while node != None:
            print(node.item , end="<->")
            node = node.prev
    
dll = DLL()

# Checking insertFirst() method
for i in range(10):
    dll.insertFirst(i)

# Checking insertEnd() method
for i in range(10,20):
    dll.insertEnd(i)

# Chekcing insertAt() method
pos = 1
for i in range(100,110):
    dll.insertAt(pos,i)
    pos += 1

# Chekcing deleteFirst() method
for i in range(5):
    dll.deleteFirst()

# Chekcing deleteEnd() method
for i in range(5):
    dll.deleteEnd()

# Checking deleteAt() method
dll.deleteAt(1)
dll.deleteAt(19)
dll.deleteAt(dll.length())
dll.deleteAt(dll.length()-(dll.length()-1))
dll.deleteAt(8)
# Checking ForDisplay method
dll.ForDisplay()
dll.getHeadTail()