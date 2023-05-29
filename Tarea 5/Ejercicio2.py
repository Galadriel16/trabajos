#Ejercicio 3: Strings intercaladas donde dos palabras del mismo tamaño se unen para crear una nueva

# def palabras_intercaladas(palabra1, palabra2):
#     if len(palabra1) != len(palabra2):
#         return "Ambas palabras deben ser del mismo tamaño"
#     salida = ""
#     for i in range(0, len(palabra1)):
#         salida += palabra1[i] + palabra2[i]
#     return salida
# palabra1 = input("Escriba la primera palabra \n")
# palabra2 = input("Escriba la segunda palabra \n")
# print(palabras_intercaladas(palabra1,palabra2))

# Ejercicio que incluye función lambda y función map para combinar letras de ambas palabras. 

def palabras_intercaladas(palabra1, palabra2): # valida que ambas palabras tengan la misma longitud o tamaño
    if len(palabra1) != len(palabra2):
        return "Ambas palabras deben ser del mismo tamaño"
    
    intercaladas = ''.join(map(lambda x, y: x + y, palabra1, palabra2)) # map() aplica la función lambda a cada par de letras de las palabras
    return intercaladas

palabra1 = input("Escriba la primera palabra:\n")
palabra2 = input("Escriba la segunda palabra:\n")
print(palabras_intercaladas(palabra1, palabra2))

# Ejemplo:
# Palabra 1: vaca  palabra 2: hola