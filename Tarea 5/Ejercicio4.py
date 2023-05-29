# Ejercicio 6: Elimina repetidos de listas creadas previamente

# lista1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8]
# lista2 = [16, 16, 16, 16, 16, 16, 16, 16]
# def num_repetidos(list):
#     salida = []
#     for item in list:
#         if item not in salida:
#             salida.append(item)
#     return salida
# print(num_repetidos(lista1))
# print(num_repetidos(lista2))


# Ejercicio con lambda, filter() y map()

lista1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8]
lista2 = [16, 16, 16, 16, 16, 16, 16, 16]

def num_repetidos(lista): 
    # La función lambda verifica si un elemento tiene una cuenta mayor a 1 en la lista original, es decir, si está repetido. 
    #Se reemplaza el ciclo for
    salida = list(filter(lambda x: lista.count(x) >= 1, lista))
    salida = list(set(salida)) # se utiliza set() para eliminar los duplicados de la lista resultante y los convierte en una nueva lista: list()
    return salida

# se imprimen ambas listas para mostrarlas sin elementos repetidos
print(num_repetidos(lista1))
print(num_repetidos(lista2))

#Ejemplo:
# lista1 = [1, 1, 1, 1, 1]
# lista2 = [4, 8, 16, 32, 32, 32]