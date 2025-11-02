from typing import List
def Partition(array:List , low , high):
    i = low
    j = high
    pivot = array[low]
    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            array[i] , array[j] = array[j] , array[i]
            
    array[low] , array[j] = array[j] , array[low]
    return j

def QuickSort(array:List , low , high):
    if low < high:
        p = Partition(array , low , high)
        QuickSort(array , low , p - 1)
        QuickSort(array , p + 1 , high)
    
    return array

array = [10 , 15 , 1 , 2 , 9 , 16 , 11]
array = [i for i in range(9 , -1 , -1)]
print(QuickSort(array , 0 , len(array) - 1))
