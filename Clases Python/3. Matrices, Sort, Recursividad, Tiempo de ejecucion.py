Matriz identidad?

from random import randint
print(randint(0, 9))

imprimir matriz

insertion sort

# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

recursividad 

factorial for vs recursivo

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

def factorial_for(x):
    fact = 1
  
    for i in range(1,x+1): 
        fact = fact * i 
    return fact




#Extra, tiempo de ejecucion

import time
start = time.time()

end = time.time()
print(end - start)