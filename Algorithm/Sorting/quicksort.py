# Ascending order
def Partition(array, l, h):
    pivot = array[l]
    i = l
    j = h

    while i < j:
        while i <= h and array[i] <= pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    array[l], array[j] = array[j], array[l]
    return j


def QuickSort(array, low, high):
    if low < high:
        p = Partition(array, low, high)
        QuickSort(array, low, p - 1)
        QuickSort(array, p + 1, high)

    return array


array = [i for i in range(9, -1, -1)]
print(QuickSort(array, 0, len(array) - 1))


# Descending order
def Partition(array , l , h):
    pivot = array[l]
    i = l
    j = h
    
    while i < j:
        while i <= j and array[i] >= pivot:
            i += 1
        
        while array[j] < pivot:
            j -= 1
        
        if i < j:
            array[i] , array[j] = array[j] , array[i]
    
    array[l] , array[j] = array[j] , array[l]
    return j

def QuickSort(array , l , h):
    if l < h:
        p = Partition(array , l , h)
        QuickSort(array , l , p - 1)
        QuickSort(array , p + 1 , h)
    
    return array

array = [i for i in range(10)]
print(array)
print(QuickSort(array , 0 , len(array) - 1))