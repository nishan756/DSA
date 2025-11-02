from typing import List , Any
def LinearSearch(array:List , data:Any):
    print('Using for loop')
    print('--------------')
    for i in range(len(array)):
        if array[i] == data:
            print(f'Data found at {i} position')
            break
    else:
        print('Not found')
    
    # Using while loop
    print('Using while loop')
    print('----------------')
    i = 0
    while i < len(array):
        if array[i] == data:
            print(f'Data found at {i} position')
            break 
        i+= 1
    else:
        print('Not found')


array = [5 , 1 , 0 , 6 , 8 , 65 , 4 , 35 , 120]
