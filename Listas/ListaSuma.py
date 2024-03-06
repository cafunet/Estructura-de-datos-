mi_lista = [1,2,3,4,5]
def sumaLista(mi_lista):
    suma = 0
    for elem in mi_lista:
        suma += elem
    return suma
print(sumaLista(mi_lista))