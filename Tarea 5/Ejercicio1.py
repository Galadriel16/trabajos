# Ejercicio 1: Se crear un triángulo con un número específico dado por el usuario con una función definida

# # def triangulo(num):
# #     if num == 0:
# #         print("Debe escribir un número mayor a 0")
# #         return
# #     triangulo_var = ""
# #     for i in range(1, num+1):
# #         triangulo_var += str(i) + " "
# #         print(triangulo_var)
# # num = int(input("Ingrese un número mayor 0: \n"))
# # triangulo(num)

# Ejercicio con la función lambda 

# Se define función lambda llamada triangulo que acepta un argumento num. Verifica si num es igual a cero y, de ser así, 
#imprime un mensaje de error. Caso contrario, genera una lista con los números y los convierte en una cadena separada por espacios mediante el método join().

triangulo = lambda num: [print('Debe escribir un número mayor a 0') if num == 0 else print(' '.join([str(i) for i in range(1, num+1)]))]

num = int(input("Ingrese un número mayor a 0:\n"))
triangulo(num)

#Ejemplos:
# num = 10