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
        for i in range(1, numero + 1): #ciclo for para introducir los números que el usuario indicó al inicio.
            valor = int(input(f"Escriba el número {i}: "))
            suma = suma + valor 
        print(f"La suma de los números que ha escrito es {suma}")

if __name__ == "__main__": #lo que entendí es que al usar este código me permite respetar el uso de las variables dentro de la función "sum"
    sum()  #no habría conflicto al momento de importar la función en otro *.py

# Función de la RESTA
def rest():
    print("RESTA DE VALORES")
    print("----------------")
    num1 = int # se asigna un número y se declara como un entero
    num2 = int # se asigna un segundo número y se declara como un entero

    num1 = int(input("Escriba el primer número: ")) # usuario escribe un número y luego repite el procedimiento con el segundo número
    num2 = int(input("Escriba el segundo número: "))
    resta = int(num1 - num2) # la variable resta guardará el resultado de restar num1 - num2
    print('El resultado de la resta es: ')
    print(resta)

if __name__ == "__main__":
    rest()


# Función de la MULTIPLICACIÓN
def multi():
    print("MULTIPLICACIÓN DE VALORES")
    print("---------------")
    numero = int(input("¿Cuántos valores va a introducir? ")) #tiene la misma lógica que la función sum

    if numero <= 0: 
        print("¡Valores deben ser mayores a cero!") #valida que los valores no sean menores o iguales a cero
    else:
        multiplica = 1 # se asigna el valor de 1 y no 0, ya que al multiplicar cero por cualquier valor que introduzca el usuario me daba cero, por eso se le asigna 1
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
    num1 = int #similar al de la función de resta
    num2 = int

    num1 = int(input("Escriba el primer número: "))
    num2 = int(input("Escriba el segundo número: "))
    division = float(num1 / num2) # se utilizan en lugar de enteros, números decimales, ya que muchas veces los resultados con división arrojan esos valores.
    print('El resultado de la división es: ')
    print(division)

if __name__ == "__main__":
    divi()

# Función del FACTORIAL
def factor():
    print("FACTORIAL DE UN VALOR")
    print("---------------------")
    numero = int(input("Escriba un número entero mayor que cero: ")) #similar a la función suma y multiplicación.

    if numero <= 0:
        print("¡Error! El número no es un entero") #valida que el número no sea un número igual o menor a cero
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
    base = int(input("Escriba el número base: ")) #usuario introduce un número para la base y otro para el exponente
    expo = int(input("Escriba el número del exponente: "))

    if base == 0 and expo == 0: # si ambos números son cero, entonces aparece un mensaje de error
        return 'No está definida'
    elif base != 0 and expo == 0: # si la base es diferente a cero, pero el exponente es cero, debe arrojar siempre un valor de 1
        return 1
    else:
        potencia = 1 #cuando el valor de la potencia se le asigna el valor de 1, entonces se crea un ciclo for para que se multiplique la base por la cantidad de veces que corresponde al exponente
        for i in range(expo):
            potencia = potencia * base
        print(f"La potencia es {potencia}.")

if __name__ == "__main__":
    poten()
