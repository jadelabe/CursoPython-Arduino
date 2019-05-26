def createMatrix(x, y): 
    fila = []
    matriz = []
    for i in range(0, x): 
        for j in range(0, y): 
            if i ==j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila.copy())
        fila.clear()
    return matriz


def main():
    mat = createMatrix(5,5)
    for i in range(0, 5): 
        print(mat[i])


if __name__ == "__main__":
    main()