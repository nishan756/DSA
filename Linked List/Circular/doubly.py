class Node:
    def __init__(self,item):
        self.item = item
        self.prev = None
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
    # Insertion
    def insertFirst(self,item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            self.tail = node

            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            node.prev  = self.tail
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.tail.next = self.head
    
    def insertEnd(self,item):
        if self.isEmpty():
            self.insertFirst(item)
        else:
            node = Node(item)
            self.tail.next  = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
    
    def insertAt(self,pos,item):
        length = self.length()
        if pos < 1 or pos > length+1:
            print("Invalid Position")
        elif pos == 1:
            self.insertFirst(item)
        elif pos == length+1:
            self.insertEnd(item)
        else:
            i = 1
            temp = self.head
            node = Node(item)
            while i < pos - 1:
                temp = temp.next
                i += 1
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
            node.prev = temp
    # Deletion
    def deleteFirst(self):
        length = self.length()
        if self.isEmpty():
            print("Can\'t delete. The Linked List is empty")
        elif length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            temp.next.prev = self.tail
            self.tail.next = temp.next
            self.head = temp.next
            del temp
    
    def deleteEnd(self):
        length = self.length()
        if self.isEmpty():
            print("Can\'t delete. The Linked List is empty")
        elif length == 1:
            self.head = None
            self.tail = None
        else:
            prevtail = self.tail
            currenttail = prevtail.prev

            currenttail.next = self.head
            self.tail = currenttail
            self.head.prev = currenttail
            del prevtail
    
    def deleteAt(self,pos):
        length = self.length()
        if pos < 1 or pos > length:
            print("Invalid Position")
        elif pos == 1:
            self.deleteFirst()
        elif pos == length:
            self.deleteEnd()
        else:
            prevnode = self.head
            i = 1
            while i < pos - 1:
                prevnode = prevnode.next
                i += 1
            target = prevnode.next
            nextnode = target.next 

            prevnode.next = nextnode
            nextnode.prev = prevnode
            del target

    def forDisplay(self):
        if self.isEmpty():
            print('The Linked List is empty')
        else:
            temp = self.head
            while temp:
                print(temp.item,end="<->")
                temp = temp.next
                if temp == self.head:
                    break
    
    def backDisplay(self):
        if self.isEmpty():
            print('The Linked List is empty')
        else:
            temp = self.tail
            while temp:
                print(temp.item,end="<->")
                temp = temp.prev
                if temp == self.tail:
                    break

dll = Circular()

# Checking insertFirst() method
for i in range(10):
    dll.insertFirst(i)

# Checking insertEnd() method
for i in range(10):
    dll.insertEnd(i)

# Checking insertAt() method
for i in range(11 , 21):
    dll.insertAt(i,i)

# Checking deleteFirst() method
for i in range(10):
    dll.deleteFirst()

# Checking deleteEnd() method
for i in range(10):
    dll.deleteEnd()

# Checking deleteAt() method
dll.deleteAt(2)
dll.deleteAt(2)
dll.deleteAt(2)
dll.deleteAt(2)
dll.deleteAt(6)
dll.deleteAt(1)
# Checking forDisplay() method
dll.forDisplay()

print(f"\nHead->Prev:{dll.head.prev.item}\nHead:{dll.head.item}\nTail:{dll.tail.item}\nTail->Prev:{dll.tail.next.item}\nLength:{dll.length()}")