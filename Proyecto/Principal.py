# Proyecto: Black Jack

#Se importa el módulo que contiene las funciones para jugar al blackjack
import usuarios
import blackjack
import cartas
import estadisticas

resulta = "Ganó"

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
            jugar = blackjack.juego([], [], cartas.crear_baraja())
        elif crear == 2:
            resultado = usuarios.seleccion_usuario() # selecciona nuevo usuario
            jugar = blackjack.juego([], [], cartas.crear_baraja())
        else:
            crear == 3 # consulta el usuario y agrega las estadísticas en el archivo creado con el nombre del usuario.
            resultado = estadisticas.agrega_estadist(usuarios.seleccion_usuario(), resulta)
            print('------Terminaste el juego-------')
            break

