#Versión 0.2:
#agregué creador de personajes y selección de rival
#Versión 0.3:
#rebalanceo de HP y fuerza: el HP se multiplicó por 10, el daño está basado en la fuerza del personaje (todavía no pude hacer mi idea de randomizarlo)
#creado un rival generado al azar, con salud entre 100 y 200, y fuerza entre 10 y 15

import random
import time

class jugador: 
    def __init__(self, HP, fuerza):
        self.HP = HP
        self.fuerza = fuerza

#Rivales
global PC  
global PC2
global PC3
global PC4 
PC = jugador(60, 8)
PC2 = jugador(100, 10)
PC3 = jugador(150, 12)
PC4 = jugador(random.randint(100, 200), random.randint(10,15))

def creacion_pj():
    puntos = 20
    print("\nBienvenido a la creación de personaje\nTendrá " + str(puntos) + " puntos que podrá asignar a cada habilidad")
    print("\nLas habilidades son:\nHP: Cuántos puntos de vida tenés (el valor que le asigne se multiplicará por 10)\nFuerza: Cuánto daño hacés al golpear\n")

    HP_pj = int(input("¿Cuántos puntos quiere asignarle a su HP?: ")) * 10
    print("Tendrá " + str(HP_pj) + (" puntos de vida"))
    print("Le quedan " + str(puntos - (HP_pj / 10)) + " puntos para asignar")
    fuerza_pj = input("¿Cuántos puntos quiere asignarle a su Fuerza?: ")
    print("Tendrá " + fuerza_pj + (" puntos de fuerza"))
    global PJ
    PJ = jugador(HP_pj, fuerza_pj) 

    if int(int(HP_pj) / 10) + int(fuerza_pj) == puntos:
        print("\n¡Su personaje ha sido creado con éxito!")
        print("\nTu personaje va a tener: \n" + str(HP_pj) + " Puntos de HP\n" + str(fuerza_pj) + " Puntos de Fuerza\n")
        print("Ahora proseguirá a elegir su rival: ")
        time.sleep(2)
        eleccion()

    elif int(int(HP_pj) / 10) + int(fuerza_pj) < puntos:
        print("\nHa utilizado menos de los puntos asignados, ¿Está seguro que quiere continuar?")
        continuar = input("Presione Y para continuar o Presione N para volver a crear su personaje: ")
        continuar = continuar.lower()
        if continuar == "y":
            eleccion()
        elif continuar == "n":
            creacion_pj()
        while (continuar != "y" and continuar != "n"):
            print(continuar)
            continuar = input("\nOpción inválidda.\nPresione Y para continuar de todos modos o presione N para volver a crear su personaje: ")
            continuar = continuar.lower()
    else:
        print("\nHa utilizado más puntos que los que tiene asignados. Intente de nuevo")
        time.sleep(1)
        creacion_pj()
        
def eleccion():
    print("\nPuedes pelear con los siguientes rivales:\nPC: Presiona 1\nPC2: Presiona 2\nPC3: Presiona 3\nRival Aleatorio: Presiona 4")
    global rival_elegido
    rival_elegido = input("\n¿Contra qué rival querés enfrentarte?: ")
    pelea()
    
def pelea(): 
    if rival_elegido == "1":
        hp_pc = int(PC.HP)
        fuerzac = int(PC.fuerza)
    elif rival_elegido == "2":
        hp_pc = int(PC2.HP)
        fuerzac = int(PC2.fuerza)
    elif rival_elegido == "3":
        hp_pc = int(PC3.HP)
        fuerzac = int(PC3.fuerza)
    elif rival_elegido == "4":
        hp_pc = int(PC4.HP)
        fuerzac = int(PC4.fuerza)

    hp_pj = int(PJ.HP) 
    fuerzaj = int(PJ.fuerza)

    while hp_pc > 0 and hp_pj > 0: # Mientras ambos peleadores tengan al menos 1 punto de HP, la pelea sigue
        if hp_pc == 0 or hp_pj == 0: # Si el HP de alguno de los dos llega a 0, se continua a la siguiente parte del código (ver si el jugador o la máquina pierde)
            continue
        print("\nTenés " + str(hp_pj) + " puntos de vida.\nTu rival tiene: " + str(hp_pc) + " puntos de vida.\n") # Printea cuánto HP tenes vos y el rival
        jugador = input("----------------------------------\nElegí: Piedra, Papel o Tijera: ") 
        jugador = jugador.lower() # Te hace elegir una acción y la transfiere a lowercase (para que no sean afectadas por usar mayusculas)

        while (jugador != "piedra" and jugador != "papel" and jugador != "tijera"): #Si el jugador no elige las tres opciones validas...
            print(jugador)                                                          #intenta preguntarte de vuelta hasta que eligas una opción valida
            jugador = input("\nOpción inválida. Elegí: Piedra, Papel o Tijera: ")
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
    
        print("Tu rival eligió: " + computer + "\n")
        if jugador == computer: 
            print("\n--¡Empate!--") 
        elif (jugador == "piedra"):                  
            if (computer == "papel"):                
                print("\n<<¡Punto para tu rival!>>\n\n¡Te quita " + str(1*fuerzac) + " puntos de vida!") 
                hp_pj = hp_pj - (1*fuerzac)                    
            else:
                print("\n||¡Punto para vos!||\n\n¡Le quitas " + str(1*fuerzaj) + " puntos de vida!")
                hp_pc = hp_pc - (1*fuerzaj)
        elif (jugador == "papel"):
            if (computer == "piedra"):
                print("\n||¡Punto para vos!||\n\n¡Le quitas " + str(1*fuerzaj) + " puntos de vida!")
                hp_pc = hp_pc - (1*fuerzaj)
            else:
                print("\n<<¡Punto para tu rival!>>\n\n¡Te quita " + str(1*fuerzac) + " puntos de vida!")
                hp_pj = hp_pj - (1*fuerzac)
        elif (jugador == "tijera"):
            if (computer == "piedra"):
                print("\n<<¡Punto para tu rival!>>\n\n¡Te quita " + str(1*fuerzac) + " puntos de vida!")
                hp_pj = hp_pj - (1*fuerzac)
            else:
                print("\n||¡Punto para vos!||\n\n¡Le quitas " + str(1*fuerzaj) + " puntos de vida!")
                hp_pc = hp_pc - (1*fuerzaj)
    
    if hp_pj < hp_pc:                                      #Si el HP del jugador es mayor al HP de la pc, ganaste (si llega acá es porque uno de los dos es 0)
        print("\n<<<Perdiste, capo, mal ahí.>>>") 
        print("----------------------------------\n")
        revancha = input("\nApretá Y si querés la revancha, o apretá N para elegir a otro rival: ")
        revancha = revancha.lower()
        
        if revancha == "y":
            pelea()
        elif revancha == "n":
            eleccion()
        while (revancha != "y" and revancha != "n"):
            print(revancha)
            revancha = input("Opción inválida.\nApretá Y si querés la revancha, o apretá N para elegir a otro rival: ")
            revancha = revancha.lower
    else:                       
        print("\n|||¡GANASTE!|||")
        input("\nApretá cualquier tecla para elegir a tu próximo rival: ")
        print("----------------------------------\n")
        eleccion()

creacion_pj()
