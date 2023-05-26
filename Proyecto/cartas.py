
from random import sample
import blackjack

class mano:
    def __init__(self, playername):
        self.playername = playername
        self.cardlist = []
        self.value = 0

# función que crea la baraja compuesta por 52 cartas y la representación de cada una con sus respectivos equivalentes
    def creadorbaraja():
        return sample([(x,y)for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']for y in ['♦','♣','♠','♥']], 52)

# función que asigna un valor a las cartas que contienen letras
    def valor(carta):
        if carta[0] == 'J' or  carta[0] == 'K' or  carta[0] == 'Q':
            return 10
        elif carta[0] == 'A':
            return 1

        else:
            return carta[0]

# contador de las cartas que se van asignando al jugador en una lista
    def contador(cardlist):
        if(len(cardlist)==0):
            return 0
        else:
            return contador(cardlist[1:])+valor(cardlist[0])

# función que comprueba los valores asignados a las cartas por el sistema
    def comprobacion(cardlist,numero):
        if cardlist == []:
            return numero
        elif cardlist[0] in [('A', '♥'),('A', '♦'),('A', '♠'),('A', '♣')] and numero+10<22:
            return comprobacion(cardlist[1:],numero+10)
        else:
            return comprobacion(cardlist[1:],numero)

# función que reparte las cartas tanto al jugador como a la casa o dealer
    def repartirIni(self, isdealer=False, cardlist):
        self.playername.append(cardlist[0])
        self.append(cardlist[20])
        isdealer.append(cardlist[1])
        print({self.playername}": " + str(self))
        print("Casa: " + str(self.cardlist))
        blackjack.juego(self, isdealer, cardlist[4:])

    def repartir(self, isdealer, cardlist, turno):
        if turno==0:
            self.playername.append(cardlist[0])
            print("Cartas jugador: " + str(self.playername))
            print("Cartas casa: " + str(isdealer))
            blackjack.juego(self.playername, isdealer, cardlist[2:])
        if turno==1:
            isdealer.append(cardlist[1])
            print("Cartas jugador: " + str(self.playername))
            print("Cartas casa: " + str(isdealer))
            blackjack.juego1(self.playername, isdealer, cardlist[2:])

    while True:
        blackjack.juego([],[],creadorbaraja())
        if(input("Desea continuar JUGANDO BLACK JACK? (Y/N)").upper() != "Y"):
            break
    
