# búsqueda_matriz.py
#crear una matriz bidimensional 3*3 con valores numéricos
matriz = [
    [5, 8, 12],
    [6, 7, 2],
    [3, 10, 9]
    ]

# función para realizar la búsqueda de un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i,j) # Retorna la posición (fila, columna) si el valor se encuentra
    return None # Retorna None si el valor no se encuentra

# Valor a buscar en la matriz
valor_a_buscar = 7

# Llamar a la función para buscar el valor
posición = buscar_valor(matriz, valor_a_buscar)

# Mostrar un mensaje adicional si el valor se encontró o no, y su posición en la matriz
if posición:
    print(f"El valor {valor_a_buscar} se econtró en la posición {posición}")
else:
    print(f"El valor {valor_a_buscar} no se encotró en la matriz")


