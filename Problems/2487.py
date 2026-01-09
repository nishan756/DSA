from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            current = head
            nextNode = current.next

            while nextNode != None:
                if nextNode.val > current.val:
                    if current == head:
                        head = nextNode
                        head.next = nextNode.next
                    current.next = None

                current = nextNode
                nextNode = current.next 




            
