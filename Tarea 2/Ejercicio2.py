# Ejercicio 2: Triángulo

def triangulo(num):
    if num == 0:
        print("Debe escribir un número mayor a 0")
        return
    triangulo_var = ""
    for i in range(1, num+1):
        triangulo_var += str(i) + " "
        print(triangulo_var)
num = int(input("Ingrese un número mayor 0: \n"))
triangulo(num)
