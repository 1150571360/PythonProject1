# ordenar_fila.py

# crear una matriz bidimencional 3*3 con valores numéricos
matriz = [
    [5, 8, 12],
    [6, 7, 2],
    [3, 10, 9]
]

# Función para ordenar una fila específicade la matriz en orden ascendente utilizando bubble sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar
fila_a_ordenar = 1 # ordenaremos la segunda fila (índice 1)

# Llamar a la función para ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
