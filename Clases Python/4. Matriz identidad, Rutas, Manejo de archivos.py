#Matriz identidad

def createMatrix(x, y): 
    fila = []
    matriz = []
    for i in range(0, x): 
        for j in range(0, y): 
          fila.append(0)
        matriz.append(r.copy())
        fila.clear()
    return m

print(createMatrix(3,3))
#Rutas
rutas relativas
./Downloads

..\..\Windows

absolutas
/etc

C:\Windows

#Manejo de archivos
open(archivo, modo)

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

extra

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

file = open("demofile.txt", "rt")

print(f.read(5))
print(f.readline())

for x in file:
  print(x)

file.close()

file.write("Now the file has more content!")

#borrar archivos !!!! CON CUIDADO !!!!!

import os
ruta = "./text.txt"
if os.path.exists(ruta):
  os.remove(ruta)
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")


https://www.w3schools.com/python/python_regex.asp

deberes: Clase matriz 
                Crear dinamica llena de 0, crear una matriz con 2 valores q le pasemos(tam_fila y tam_columna)
                Rellenar 0, llenar todas las posiciones con 0
                Insertar elemento en la matriz pasamos 3 valores, y nos guarda el valor en la posicion q indican los otros 2
                Devolver matriz
          Usar esta clase desde otro .py
