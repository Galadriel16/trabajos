# Ejercicio 1: Función que imprime en pantalla todos los números, letras y caracteres especiales presentes en una string. 

def caracteres_contador(cadena):
    # variables que asignan los tipos de caracteres solicitados. Se asigna un valor de cero inicialmente.
    letras = 0
    numeros = 0
    caracteres = 0

    #Ciclo for que valida los caracteres que se introducen en la palabra solicitada al usuario. 
    for i in cadena: 
        if i.isalpha(): #Lee la cadena de caracteres y si detecta una letra suma un 1
            letras += 1
        elif i.isdecimal(): #Lee la cadena de caracteres y si detecta un número suma un 1
            numeros += 1
        else: #sino es ninguna de las anteriores, suma un 1, esto aplica para los caracteres especiales
            caracteres += 1
            pass
    
    return letras, numeros, caracteres 

texto = input('Ejercicio 1: Digite una palabra ')           
resultado = caracteres_contador(texto)

#Imprime en pantalla el contador de cada uno de los elementos que conforman el texto introducido por el usuario
print('Letras: %i' % resultado[0])
print('Números: %i' % resultado[1])
print('Caracteres: %i' % resultado[2])
print ('---------------------------------------------------------------------------------------')

#EJEMPLO DE PRUEBA: EJERCICIO 1
#Ejemplo_1: @v3na
#Ejemplo_2: N0sotr0s
#Ejemplo_3: !!!!Pasaporte!!!!"_@_@"
#Ejemplo_4: BANC0_D3_D@T05

#---------------------------------------------------------------------------------------

# Ejercicio 2: 
#Función que cuenta todas las letras repetidas en una palabra que se introduce por teclado.

def contador_repetidas(letra):
# El usuario introduce la palabra que se validará en el programa
    palabra = 0

palabra  = input(str("Ejercicio 2: Escriba una palabra:  "))
diccionario = { } # se crea una lista que permanecerá en blanco y se llamará diccionario

for letra in palabra: # ciclo for para validar la cantidad de letras que aparecen repetidas en la palabra
    if letra in diccionario: # si la letra aparece en la lista, se le va a sumar uno
        diccionario[letra] = diccionario [letra] + 1 
    else:
        diccionario[letra] = 1 # si la letra no se repite, se le asignará un valor de 1

print("%sResultado: %s" % (letra, diccionario)) # Imprime en pantalla la letra y cuántas veces se repite
print ('---------------------------------------------------------------------------------------')

#EJEMPLO DE PRUEBA: EJERCICIO 2
#Ejemplo_1: Amigos
#Ejemplo_2: L3t5_do_IT
#Ejemplo_3: Estamos bien
#Ejemplo_4: Categoría21aa

#---------------------------------------------------------------------------------------
# Ejercicio 3: 
#Función que elimina todas las apariciones de un elemento en una lista


#---------------------------------------------------------------------------------------
# Ejercicio 4: 
#Función que recibe una secuencia de números e imprime una lista y una tupla con valores definidos por el usuario

def lista_tupla(entrada):

    lista = entrada.split(',')  # Los números son dados separados por coma.
   
    # Convierte los valores a enteros.
    for i in range(len(lista)):
        lista[i] = int(lista[i])
      #  tupla = tuple(lista)
    return lista #tupla

lista = input("Ejercicio 4: Escriba una lista de números, separados por coma :")
#tupla = {''}
resultado = lista_tupla(lista) 
#resultado = lista_tupla(tupla) 
print ("Lista: ", [lista])
#print ("Tupla: ", {tupla})
print ('---------------------------------------------------------------------------------------')

#EJEMPLO DE PRUEBA: EJERCICIO 4
#Ejemplo_1: 1,2,3,4,5,6,5,2
#Ejemplo_2: 4,5,5,5,5,6,2,1,3,5
#Ejemplo_3: 1,5,7,3
#Ejemplo_4: 2,2,2,2,2,2,2,2
