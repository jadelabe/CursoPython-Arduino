#Casting
x = int(1)   # x will be 1
y = float(2.8)   # y will be 2.8
z = str(3.0)  # z will be '3.0'

#Operators

#+	Addition	x + y	
#-	Subtraction	x - y	
#*	Multiplication	x * y	
#/	Division	x / y	
#%	Modulus	x % y 10%2	
#**	Exponentiation	x ** y	 
#//	Floor division	x // y


#==	Equal	x == y	
#!=	Not equal	x != y	
#>	Greater than	x > y	
#<	Less than	x < y	
#>=	Greater than or equal to	x >= y	
#<=	Less than or equal to	x <= y

#and or  and not
#in not in

#Arrays
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

colores = ["rojo", "azul", "amarillo"]
colores[1] = "naranja"
print(colores)
len(colores)

for x in colores:
    print(x)

colores.append("verde")
colores.pop()
colores.insert(1, "rosa")

colores.remove("amarillo")
del colores[5]
colores.clear()
del colores

#Docs


#If-Else 
a = 2
b = 20
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

  #For
for x in range(2, 30, 3):
    print(x)

#While
i = 1
while i < 6:
    print(i)
    i += 1
i = 3 
while True:
    print("hola")