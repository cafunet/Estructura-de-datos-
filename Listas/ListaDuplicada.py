def duplicado(lista):
    lista1 = []
    for elem in lista:
        if elem not in lista1:
            lista1.append(elem)
    return lista1
print(duplicado([1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8]))
