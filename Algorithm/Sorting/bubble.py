from typing import List
def BubbleSort(array:List , sort_type = 'asc'):
    if sort_type == 'asc':
        for i in range(len(array) - 1):
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

    elif sort_type == 'dsc':
        for i in range(len(array) - 1):
            for j in range(len(array) - 1 - i):
                if array[j] < array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

    else:
        raise ValueError('Invalid sorting type')
    
    return array
asc_array = [i for i in range(10)]
dsc_array = [i for i in range(9 , -1 , -1)]

print('Descending:',BubbleSort(asc_array,'dsc'))
print('Ascending:',BubbleSort(dsc_array,'asc'))