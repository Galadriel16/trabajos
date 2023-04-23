# Ejercicio 6: Elimina repetidos

lista1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8]
lista2 = [16, 16, 16, 16, 16, 16, 16, 16]
def num_repetidos(list):
    salida = []
    for item in list:
        if item not in salida:
            salida.append(item)
    return salida
print(num_repetidos(lista1))
print(num_repetidos(lista2))