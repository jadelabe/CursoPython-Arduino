
import time
start = time.time()

y = int(input())

for x in range(1,y+1):
    p=(y+1)-x
    for patata in range(1,p+1):
        print(" ", end = '')
    z = 1+(2*(x-1))
    for calabazin in range(1, z+1):
        print("*", end = '')
    print("")

for calabazin in range(1, z+3):
    print("*", end = '')
print("")

for x in range(y+1,1,-1):
    p=y+1-x
    for patata in range(1,p+2):
        print(" ", end = '')
    z = 1+(2*(x-1))
    for calabazin in range(1, z-1):
        print("*", end = '')
    print("")

end = time.time()
print(end - start)