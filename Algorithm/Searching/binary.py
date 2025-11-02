from typing import List , Any
def BinarySearch(array:List , data:Any):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == data:
            print(f'{data} found at {mid} index')
            break
        elif data > array[mid]:
            left = mid+1
        else:
            right = mid - 1
    else:
        print('Not found')

array = [i for i in range(10)]
for i in range(12):
    BinarySearch(array,i)