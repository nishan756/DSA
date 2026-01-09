from typing import List
class MaxHeap:
    def __init__(self) ->None:
        self.heap_array = []

    def swap(self , i:int , j:int) ->None:
        self.heap_array[i] , self.heap_array[j] = self.heap_array[j] , self.heap_array[i]

    def heapify(self , index:int) ->None:
        length = len(self.heap_array)
        new_index = index
        left = 2 * new_index + 1
        right = 2 * new_index + 2

        if (left < length) and (self.heap_array[new_index] < self.heap_array[left]):
            new_index = left
        
        if (right < length ) and (self.heap_array[new_index] < self.heap_array[right]):
            new_index = right
        
        if new_index != index:
            self.swap(new_index , index)
            self.heapify(new_index)

    def performHeapify(self) ->None:
        n = len(self.heap_array)
        for i in range((n // 2) - 1 , -1 , -1):
            self.heapify(i)

    def insertHeap(self , value) ->None:
        self.heap_array.append(value)

        '''
        index = len(self.heap_array) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap_array[parent] < self.heap_array[index]:
                self.swap(parent , index)
                index = parent
            else:
                return
        '''

        # We can also call the performHeapify() method
        self.performHeapify()
    
    def heapSort(self):
        self.performHeapify()

        n = len(self.heap_array) - 1
        for i in range(n , 0 , -1):
            self.heap_array[i] , self.heap_array[0] = self.heap_array[0] , self.heap_array[i]
            self.heapify(i)


    def viewHeap(self) ->List:
        return self.heap_array

    def getLargest(self) ->int:
        return self.heap_array[0] if len(self.heap_array) != 0 else 0

max_heap = MaxHeap()
for i in range(10):
    max_heap.insertHeap(i)

print("Max Heap:")
print(max_heap.viewHeap())
print("Larget element:")
print(max_heap.getLargest())
max_heap.heapSort()
print(max_heap.viewHeap())


# class MinHeap(MaxHeap):
    
#     def heapify(self , index):
#         # Length of the array
#         length = len(self.heap_array)

#         # Current node index 
#         current = index

#         # Left and right child node index
#         left = 2 * current + 1
#         right = 2 * current + 2

#         if (left < length) and (self.heap_array[current] > self.heap_array[left]):
#             current = left
        
#         if right < length and (self.heap_array[current] > self.heap_array[right]):
#             current = right

#         if current != index:
#             self.swap(current , index)
#             self.heapify(current)
    
#     def insertHeap(self, value):
#         self.heap_array.append(value)
#         index = len(self.heap_array) - 1

#         '''
#         while index > 0:
#             parent = ( index - 1 ) // 2
#             if self.heap_array[parent] > self.heap_array[index]:
#                 self.swap(parent , index)
#                 index = parent
#             else:
#                 return
#         '''
#         self.performHeapify()
    
#     def getSmallest(self):
#         return self.heap_array[0] if len(self.heap_array) != 0 else 0
    

# min_heap = MinHeap()
# for i in range(10 , -1 , -1):
#     min_heap.insertHeap(i)
# print(min_heap.viewHeap())
# print(min_heap.getSmallest())

