from random import sample
import cartas
import estadisticas
import usuarios

# función que le indica al jugador si desea continuar jugando o no, de acuerdo con la selección de cartas repartidas

def juego(lJugador, lCasa, lista):
    print(lJugador)
    if len(lJugador) == 0 and len(lCasa) == 0:
        cartas.repartirIni(lJugador, lCasa, lista)
        return "primera"
    else:
        if cartas.contador(lJugador) <= 21:
            if input("¿Desea continuar?: (Y/N)").upper() != "N":
                cartas.repartir(lJugador, lCasa, lista, turno=0)
            else:
                print("SU PUNTAJE ES", cartas.comprobacion(lJugador, cartas.contador(lJugador)))
                cartas.repartir(lJugador, lCasa, lista, turno=1)
        else:
            return print("Perdió el JUGADOR, tiene:", cartas.comprobacion(lJugador, cartas.contador(lJugador)))

# función que define las cartas seleccionadas e indica si el jugador perdió o ganó
def juego1(lJugador, lCasa, lista):
    if cartas.comprobacion(lCasa, cartas.contador(lCasa)) <= 21:
        print("CASA SU PUNTAJE ES ", cartas.comprobacion(lCasa, cartas.contador(lCasa)))
        if cartas.comprobacion(lCasa, cartas.contador(lCasa)) < cartas.comprobacion(lJugador, cartas.contador(lJugador)):
            cartas.repartir(lJugador, lCasa, lista, 1)
        elif cartas.comprobacion(lCasa, cartas.contador(lCasa)) >= cartas.comprobacion(lJugador, cartas.contador(lJugador)):
            print("La casa ganó: " + str(cartas.comprobacion(lCasa, cartas.contador(lCasa))) + " a " + str(cartas.comprobacion(lJugador, cartas.contador(lJugador))))
            estadisticas.agrega_estadist(usuarios.seleccion_usuario(), 'Perdió')
            return "final"
        elif cartas.comprobacion(lJugador, cartas.contador(lJugador)) >= cartas.comprobacion(lCasa, cartas.contador(lCasa)):
            print(f'El jugador {usuarios.seleccion_usuario().upper()}' + str(cartas.comprobacion(lJugador, cartas.contador(lJugador))) + " a " + str(cartas.comprobacion(lCasa, cartas.contador(lCasa))))
            estadisticas.agrega_estadist(usuarios.seleccion_usuario(), 'Ganó')
            return "final"
    else:
        return print("Perdió la CASA, tiene: " + str(cartas.comprobacion(lCasa, cartas.contador(lCasa))))
