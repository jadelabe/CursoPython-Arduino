from random import randint


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def create_vector(a, b):
    vector = []
    for x in range(a):
        vector.append(randint(0,20))
    print(vector)
    print(insertionSort(vector))

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
    return arr

def no_such_action():
    print("Valor incorrecto")

def main():
    actions = {"+": suma, "-":resta, "*": multiplicacion, "s":create_vector}
    while 1:
        print("Introduzca los 2 numeros y la operacion ")
        a = int(input())
        b = int(input())
        selection = input("Operacion: ")
        if "e" == selection:  #condicion de salida
            return
        print(actions.get(selection, no_such_action)(a, b))

if __name__ == "__main__":
    main()