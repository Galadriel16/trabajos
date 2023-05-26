# Proyecto: Black Jack

#Se importa el módulo que contiene las funciones para jugar al blackjack
import usuarios

# Menú donde el usuario escogerá la operación que desea realizar

while True:
    print('B L A C K  J A C K')
    print('------------------')
    print('1. Crear nuevo usuario')
    print('2. Seleccionar un usuario')
    print('3. Salir')

    crear = int(input ('¿Cuál opción vas a escoger? '))

    if crear == 1:
        resultado = usuarios.crear_usuario() #se crea un nuevo usuario
    elif crear == 2:
        resultado = usuarios.seleccion_usuario()
    elif crear == 3:
        print('------Terminaste el juego-------')
        break