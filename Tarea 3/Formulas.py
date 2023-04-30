# Módulo que contiene las fórmulas aritméticas y que se llama desde el archivo Principal.py


def suma(): #se define una función para la fórmula de la suma
    num = int(input('Escriba un número: '))
    sum = 0
while num  >= 0:
    sum += num
    num = int(input ("Escriba otro número: "))
     sum += num
    if num <
        return "¿Desea introducir otro número?"
    elif num == 0:
        return 1
    else 

# def main():
#     print("SUMA DE NÚMEROS")
#     numero = int(input("Escriba un número: "))
#     suma = 0
#     while numero >= 0:
#         suma += numero
#         numero = int(input("Escriba otro número: "))
#     print()
#     print(f"La suma de los números positivos introducidos es {suma}.")


# if __name__ == "__main__":
#     main()