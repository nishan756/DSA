from typing import List
def Selection(array:List , sort_type = 'asc'):
    for i in range(len(array)):
        minimum = i
        for j in range(i +1 , len(array)):
            if sort_type == 'asc':
                if array[j] < array[minimum]:
                    minimum = j
            elif sort_type == 'dsc':
                if array[j] > array[minimum]:
                    minimum = j
            else:
                raise ValueError("Invalid sorting type")
        
        (array[i] , array[minimum]) = (array[minimum] , array[i])
    
    return array
array = [2 , 7 , 1 , 0 , 6 , 15 , 21 , 4]
print(Selection(array))
