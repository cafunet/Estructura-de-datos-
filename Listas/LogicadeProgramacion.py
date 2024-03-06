#Suma de elementos en la lista
mi_lista = [1,2,3,4,5]
def sumaLista(mi_lista):
    suma = 0
    for elem in mi_lista:
        suma += elem
    return suma
print(sumaLista(mi_lista))

#ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos del arreglo
    for i in range(n):
        # Los últimos i elementos ya están en posición
        for j in range(0, n-i-1):
            # Recorrer el arreglo desde 0 hasta n-i-1
            # Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

#buscar elemento maximo en la lista
lista = [23,4,56,7,8,9,12]
def Maximo(mas):
    numeromax= max(mas)
    return numeromax
print("el numero maximo de la lista es: ", Maximo(lista))

#fibonacci
a = 0
b = 1
i = 0
print(a)

for i in range(10):
    a_guardado = a
    a = b
    b = a_guardado + b

    print(a)
    i = i + 1

#Ordenamiento por seleccion
lista = [23, 4, 56, 7, 8, 9, 12]

def ordenamiento_seleccion(my_lista):
    for i in range(len(my_lista)-1):
        menor = i
        for n in range(1+i,len(my_lista)):
            if my_lista[n] < my_lista[menor]:
                menor=n
        if menor !=i:
            my_lista[menor], my_lista[i]= my_lista[i], my_lista[menor]
ordenamiento_seleccion(lista)
print("la lista ordenada es: ", lista)

#Buscar elemento objetivo en un arreglo que devuelva true o false
def buscar_elemento(lista, objetivo):
    for num in lista:
        if num == objetivo:
            return True
    return False
#Ejemplo de uso
lista = [23, 4, 56, 7, 8, 9, 12]
objetivo = 8
print("el numero ", objetivo, "esta presente en el arreglo? ", buscar_elemento(lista, objetivo))

#Eliminar duplicados
lista = [1, 3, 4, 1, 2, 3, 4, 7, 6]

def duplicado(lista):
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
    return lista
mi_lista = duplicado(lista)
print(mi_lista)

#multiplicar matrices
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
    True

#ordenamiento rapido Quicksort
lista = [23, 4, 56, 7, 8, 9, 12]
def QuickSort(numeros, izq, der):

    pivote = numeros[izq]
    i = izq
    j = der
    aux = 0

    while i < j:
        while numeros[i] <= pivote and i < j:
            i += 1

        while numeros[j] > pivote:
            j -= 1

        if i < j:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

    numeros[izq] = numeros[j]
    numeros[j] = pivote

    if izq < j - 1:
        QuickSort(numeros, izq, j - 1)

    if j + 1 < der:
        QuickSort(numeros, j + 1, der)

QuickSort(lista, 0, len(lista) - 1)
print(lista)

#Buscar subcadena
def buscar_elemento(lista, objetivo):
    for num in lista:
        if num == objetivo:
            return True
    return False
#Ejemplo de uso
lista = [23, 4, 56, 7, 8, 9, 12]
objetivo = 8
print("el numero ", objetivo, "esta presente en el arreglo? ", buscar_elemento(lista, objetivo))

#invertir arreglo
mi_lista=[3,4,7,9,10,15]
def inverti_lista(mi_lista):
    return mi_lista[::-1]
lista_invertida=inverti_lista(mi_lista)
print("mi lista: ",mi_lista)
print("lista invertida: ", lista_invertida)

#Contar ocurrencias
