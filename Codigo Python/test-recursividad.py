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
factorial(900)
end = time.time()
print(end - start)

start = time.time()
factorial_for(900)
end = time.time()
print(end - start)