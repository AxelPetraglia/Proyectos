import random

class jugador: # Una clase "jugador" con la cualidad de HP (por ahora)
    def __init__(self, HP):
        self.HP = HP

# Dos jugadores basados en la clase "jugador"
PJ = jugador(5) 
PC = jugador(5)

def eleccion(): #Este es el juego en sí

    hp_pj = int(PJ.HP) # La salud de los personajes, basado en cuanto hp tienen los objetos PJ/PC. Durante la pelea estos valores se reducen según quien pierde o gana.
    hp_pc = int(PC.HP)

    while hp_pc > 0 and hp_pj > 0: # Mientras ambos peleadores tengan al menos 1 punto de HP, la pelea sigue
        if hp_pc == 0 or hp_pj == 0: # Si el HP de alguno de los dos llega a 0, se continua a la siguiente parte del código (ver si el jugador o la máquina pierde)
            continue
        print("\nTenés " + str(hp_pj) + " puntos de vida.\nTu rival tiene: " + str(hp_pc) + " puntos de vida.\n") # Printea cuánto HP tenes vos y el rival
        jugador = input("----------------------------------\nElegí: Piedra, Papel o Tijera: ") 
        jugador = jugador.lower() # Te hace elegir una acción y la transfiere a lowercase (para que no sean afectadas por usar mayusculas)

        while (jugador != "piedra" and jugador != "papel" and jugador != "tijera"): #Si el jugador no elige las tres opciones validas...
            print(jugador)                                                          #intenta preguntarte de vuelta hasta que eligas una opción valida
            jugador = input("Opción inválida. Elegí: Piedra, Papel o Tijera: ")
            jugador = jugador.lower()

        computerInt = random.randint(0,2) # Hace que la computadora eliga un movimiento al azar. Como son tres movimientos posibles, 
        if (computerInt == 0):            # elige entre 3 numeros y despues el numero se traduce a un movimiento (expresado en texto)
            computer = "piedra"
        elif (computerInt == 1):
            computer = "papel"
        elif (computerInt == 2):
            computer = "tijera"
        else:
            computer = "error"    

        if jugador == computer: # Si el jugador y la computadora eligen la misma acción, se declara empate
            print("\n--¡Empate!--") 
        elif (jugador == "piedra"):                  # Si el jugador elige piedra,
            if (computer == "papel"):                # y la computadora elige papel,
                print("\n<<¡Punto para tu rival!>>") # declara que gana la computadora
                hp_pj = hp_pj - 1                    # y le resta 1 a tu HP
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
    if hp_pj < hp_pc:                                      #Si el HP del jugador es mayor al HP de la pc, ganaste (si llega acá es porque uno de los dos es 0)
        print("\n<<<Perdiste, capo, mal ahí.>>>") 
        input("\nApretá cualquier tecla para probar de vuelta: ")
        print("----------------------------------\n")
        eleccion()
    else:                       
        print("\n|||¡GANASTE!|||")
        input("\nApretá cualquier tecla para probar de vuelta: ")
        print("----------------------------------\n")
        eleccion()

eleccion()
