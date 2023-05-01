# Tarea 3: Calculadora

#Se importa el módulo que contiene las operaciones artiméticas que se realizarán en el programa
import Formulas

#Formulas.sum()
#Formulas.resta

# Se crea un menú para que el usuario escoja la operación que desea realizar

while 1:
    print('C A L C U L A D O R A ')
    print('----------------------')
    print('Selecciona en el siguiente menú la operación que querés realizar: ')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Factorial')
    print('6. Potencia')
    print('7. Salir')

    n = int(input ('¿Cuál opción vas a escoger? '))

    if n == 1:
        resultado = Formulas.sum() #se realiza la fórmula de cada módulo proveniente del archivo Formulas.py
        file = open("resultados.txt","a") #se crea un archivo .txt que muestra la operación escogida por el usuario.
        file.write(" USUARIO ESCOGIÓ OPCIÓN 1: SUMA ")
        file.write("------------------------------")
        file.close()
    elif n == 2:
        resultado = Formulas.rest()
        file = open("resultados.txt","a")
        file.write(" USUARIO ESCOGIÓ OPCIÓN 2: RESTA ")
        file.write("-------------------------------")
        file.close()
    elif n == 3:
        resultado = Formulas.multi()
        file = open("resultados.txt","a")
        file.write(" USUARIO ESCOGIÓ OPCIÓN 3: MULTIPLICACIÓN ")
        file.write("------------------------------------------")
        file.close()
    elif n == 4:
        resultado = Formulas.divi()
        file = open("resultados.txt","a")
        file.write(" USUARIO ESCOGIÓ OPCIÓN 4: DIVISIÓN ")
        file.write("------------------------------------")
        file.close()
    elif n == 5:
        resultado = Formulas.factor()
        file = open("resultados.txt","a")
        file.write(" USUARIO ESCOGIÓ OPCIÓN 5: FACTORIAL ")
        file.write("-------------------------------------")
        file.close()
    elif n == 6:
        resultado = Formulas.poten()
        file = open("resultados.txt","a")
        file.write(" USUARIO ESCOGIÓ OPCIÓN 6: POTENCIA ")
        file.write("------------------------------------")
        file.close()
    elif n == 7:
        print('------Terminaste de usar la calculadora-------')
        break