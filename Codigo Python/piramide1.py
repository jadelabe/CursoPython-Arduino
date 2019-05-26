import time
start = time.time()

a = int(input()) + 1

b = a +(a-1)

for x in range( a - 1 , 0, -1):
    for y in range(0, x):
        print(" ", end = '')
    c = b - (2 * x)
    for z in range(0, c):
        print("*", end = '')
    print()

for x in range(0, a):
    for y in range(0, x):
        print(" ", end = '')
    c = b - (2 * x)
    for z in range(0, c):
        print("*", end = '')
    print()

    
end = time.time()
print(end - start)