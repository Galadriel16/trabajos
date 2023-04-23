#Ejercicio 3: Strings intercaladas

def palabras_intercaladas(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return "Ambas palabras deben ser del mismo tamaño"
    salida = ""
    for i in range(0, len(palabra1)):
        salida += palabra1[i] + palabra2[i]
    return salida
palabra1 = input("Escriba la primera palabra \n")
palabra2 = input("Escriba la segunda palabra \n")
print(palabras_intercaladas(palabra1,palabra2))