def multiplicar_matrices(matriz1, matriz2):
    # Verificar si las dimensiones son adecuadas para la multiplicación
    if len(matriz1[0]) != len(matriz2):
        print("No se pueden multiplicar las matrices. Las dimensiones no son compatibles.")
        return None

    # Inicializar una matriz resultante llena de ceros
    resultado = []

    # Realizar la multiplicación de matrices
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)

    return resultado

# Ejemplo de uso
matriz1 = [[1, 2],
           [3, 4]]
matriz2 = [[5, 6],
           [7, 8]]

resultado = multiplicar_matrices(matriz1, matriz2)
if resultado:
    print("El resultado de la multiplicación de las matrices es:")
    for fila in resultado:
        print(fila)
