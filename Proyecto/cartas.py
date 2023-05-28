
from random import sample
import blackjack

# Crea baraja con caracteres representativos de cada carta y asigna valores a cartas que representan letras
def crear_baraja():
    return sample([(x, y) for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['♦', '♣', '♠', '♥']], 52)

def valor(carta):
    if carta[0] in ['J', 'K', 'Q']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return carta[0]

# Contador que va asignando valores a una lista
def contador(lista):
    if len(lista) == 0:
        return 0
    else:
        return contador(lista[1:]) + valor(lista[0])

# Función que va asignando el valor de 11 a las barajas que representan la letra A
def comprobacion(lista, numero):
    if lista == []:
        return numero
    elif lista[0] in [('A', '♥'), ('A', '♦'), ('A', '♠'), ('A', '♣')] and numero + 10 < 22:
        return comprobacion(lista[1:], numero + 10)
    else:
        return comprobacion(lista[1:], numero)

# Función que reparte las cartas al inicio al jugador y la computadora
def repartir_inicial(lJugador, lCasa, lista):
    lJugador.append(lista[0])
    lJugador.append(lista[20])
    lCasa.append(lista[1])
    print("Cartas jugador: " + str(lJugador))
    print("Cartas casa: " + str(lCasa))
    jugar(lJugador, lCasa, lista[4:])

# Función que valida si el jugador desea seguir jugando o no
def repartirIni(lJugador, lCasa, lista):
    lJugador.append(lista[0])
    lJugador.append(lista[20])
    lCasa.append(lista[1])
    print("Cartas jugador:", lJugador)
    print("Cartas casa:", lCasa)
    blackjack.juego(lJugador, lCasa, lista[4:])

def repartir(lJugador, lCasa, lista, turno):
    if turno == 0:
        lJugador.append(lista[0])
        print("Cartas jugador:", lJugador)
        print("Cartas casa:", lCasa)
        blackjack.juego(lJugador, lCasa, lista[2:])
    if turno == 1:
        lCasa.append(lista[1])
        print("Cartas jugador:", lJugador)
        print("Cartas casa:", lCasa)
        blackjack.juego1(lJugador, lCasa, lista[2:])


