#Módulos de fórmulas matemáticas

#Función de la SUMA
def sum():
    print("SUMA DE VALORES")
    print("---------------")
    numero = int(input("¿Cuántos valores va a introducir? ")) # cantidad de números que se van a sumar

    if numero <= 0:
        print("¡Valores deben ser mayores a cero!") # validación, los números deben ser mayores a cero
    else:
        suma = 0
        for i in range(1, numero + 1): 
            valor = int(input(f"Escriba el número {i}: "))
            suma = suma + valor
        print(f"La suma de los números que ha escrito es {suma}")

if __name__ == "__main__":
    sum()

# Función de la RESTA
def rest():
    print("RESTA DE VALORES")
    print("----------------")
    num1 = int
    num2 = int

    num1 = int(input("Escriba el primer número: "))
    num2 = int(input("Escriba el segundo número: "))
    resta = int(num1 - num2)
    print('El resultado de la resta es: ')
    print(resta)

if __name__ == "__main__":
    rest()


# Función de la MULTIPLICACIÓN
def multi():
    print("MULTIPLICACIÓN DE VALORES")
    print("---------------")
    numero = int(input("¿Cuántos valores va a introducir? "))

    if numero <= 0:
        print("¡Valores deben ser mayores a cero!")
    else:
        multiplica = 1
        for i in range(1, numero + 1):
            valor = int(input(f"Escriba el número {i}: "))
            multiplica = multiplica * valor
        print(f"La multiplicación de los números que ha escrito es {multiplica}")

if __name__ == "__main__":
    multi()

# Función de la DIVISIÓN
def divi():
    print("DIVISIÓN DE VALORES")
    print("----------------")
    num1 = int
    num2 = int

    num1 = int(input("Escriba el primer número: "))
    num2 = int(input("Escriba el segundo número: "))
    division = float(num1 / num2)
    print('El resultado de la división es: ')
    print(division)

if __name__ == "__main__":
    divi()

# Función del FACTORIAL
def factor():
    print("FACTORIAL DE UN VALOR")
    print("---------------------")
    numero = int(input("Escriba un número entero mayor que cero: "))

    if numero <= 0:
        print("¡Error! El número no es un entero")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial = factorial * i
        print(f"El factorial de {numero} es {factorial}.")

if __name__ == "__main__":
    factor()

# Función de la POTENCIA
def poten():
    print("POTENCIA DE UN VALOR")
    print("---------------------")
    base = int(input("Escriba el número base: "))
    expo = int(input("Escriba el número del exponente: "))

    if base == 0 and expo == 0:
        return 'No está definida'
    elif base != 0 and expo == 0:
        return 1
    else:
        potencia = 1
        for i in range(expo):
            potencia = potencia * base
        print(f"La potencia es {potencia}.")

if __name__ == "__main__":
    poten()
