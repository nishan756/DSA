from typing import List
def Insertion(array:List , sort_tyoe = 'asc'):
    for i in range(1 , len(array)):
        current = array[i]
        prev = i - 1
        if sort_tyoe == 'asc':
            while prev >= 0 and current < array[prev]:
                array[prev + 1] = array[prev]
                prev -= 1
        
        elif sort_tyoe == 'dsc':
            while prev >= 0 and current > array[prev]:
                array[prev + 1] = array[prev]
                prev -= 1
        
        else:
            raise ValueError("Invalid sort type")

        array[prev + 1] = current
    return array

asc_array = [i for i in range(10)]
dsc_array = [i for i in range(9 , -1 , -1)]

print("Ascending Array:",Insertion(dsc_array))
print("Descending Array:",Insertion(asc_array , 'dsc'))
