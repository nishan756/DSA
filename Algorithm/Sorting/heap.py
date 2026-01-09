def heapify(arr , length , index):
    largest = index
    left = ( 2 * largest ) + 1
    right = ( 2 * largest ) + 2

    n = length

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest] , arr[index] = arr[index] , arr[largest]
        heapify(arr , length , largest)

def heapSort(arr):
    n = len(arr)

    for i in range((len(arr) // 2) - 1 , -1 , -1):
        heapify(arr , n , i)
    
    for j in range((n - 1) , 0 , -1):
        arr[j] , arr[0] = arr[0] , arr[j]
        heapify(arr , j , 0)

    return arr

arr = [i for i in range(10 , -1 , -1)]
print(heapSort(arr))