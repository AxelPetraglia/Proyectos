import random

class jugador:
    def __init__(self, HP):
        self.HP = HP

PJ = jugador(5)
PC = jugador(5)

def eleccion():

    hp_pj = int(PJ.HP)
    hp_pc = int(PC.HP)

    while hp_pc > 0 and hp_pj > 0:
        if hp_pc == 0 or hp_pj == 0:
            continue
        print("\nTenés " + str(hp_pj) + " puntos de vida.\nTu rival tiene: " + str(hp_pc) + " puntos de vida.\n")
        jugador = input("----------------------------------\nElegí: Piedra, Papel o Tijera: ")
        jugador = jugador.lower()

        while (jugador != "piedra" and jugador != "papel" and jugador != "tijera"):
            print(jugador)
            jugador = input("Opción inválida. Elegí: Piedra, Papel o Tijera: ")
            jugador = jugador.lower()

        computerInt = random.randint(0,2)
        if (computerInt == 0):
            computer = "piedra"
        elif (computerInt == 1):
            computer = "papel"
        elif (computerInt == 2):
            computer = "tijera"
        else:
            computer = "error"    

        if jugador == computer:
            print("\n--¡Empate!--") 
        elif (jugador == "piedra"):
            if (computer == "papel"):
                print("\n<<¡Punto para tu rival!>>")
                hp_pj = hp_pj - 1
            else:
                print("\n||¡Punto para vos!||")
                hp_pc = hp_pc - 1
        elif (jugador == "papel"):
            if (computer == "piedra"):
                print("\n||¡Punto para vos!||")
                hp_pj = hp_pj - 1
            else:
                print("\n<<¡Punto para tu rival!>>")
                hp_pc = hp_pc - 1
        elif (jugador == "tijera"):
            if (computer == "piedra"):
                print("\n<<¡Punto para tu rival!>>")
                hp_pj = hp_pj - 1
            else:
                print("\n||¡Punto para vos!||")
                hp_pc = hp_pc - 1
    if hp_pc == 0:
        print("\n<<<Perdiste, capo, mal ahí.>>>") 
        input("\nApretá cualquier tecla para probar de vuelta: ")
        print("----------------------------------\n")
        eleccion()
    if hp_pj == 0:  
        print("\n|||¡GANASTE!|||")
        input("\nApretá cualquier tecla para probar de vuelta: ")
        print("----------------------------------\n")
        eleccion()

eleccion()