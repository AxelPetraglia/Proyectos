#Versión 0.2:
#agregué creador de personajes y selección de rival

#Versión 0.3:
#rebalanceo de HP y fuerza: el HP se multiplicó por 10, el daño está basado en la fuerza del personaje (todavía no pude hacer mi idea de randomizarlo)
#creado un rival generado al azar, con salud entre 100 y 200, y fuerza entre 10 y 15

#Versión 0.3.1
#Agregada opción para ponerte nombre
#Los rivales IA ahora tienen nombres (posiblemente temporales) y son mencionados durante la pelea

#Versión 0.4
#Añadido el stat de defensa
#El daño realizado es calculado entre la fuerza del atacante y la defensa del defensor: 
#A la fuerza del atacante se le resta un número elegido entre 0 y la mitad de los puntos de defensa del que recibe el golpe

#Ejemplo: el atacante tiene 15 de fuerza y el defensor tiene 10 de defensa. 
#El randomizador elige un número entre 0 y la mitad de los puntos de defensa (5 en este caso)
#El daño causado en esta circunstancia puede variar entre 10 y 15

#Versión 0.4b
#Cambiado la fórmula para calcular daño, ahora es Daño = 2*Fuerza - randint(defensa/2, defensa*2)
#En la creación de personaje hay un mínimo de 1 para todos los stats (10 para HP)
#Ya no se pueden elegir valores negativos en la creación de persnaje
#Solucionados algunos errores en la creación de personaje

#Versión 0.4c
#Arreglado error cuando elegís algo que no sea y o n cuando te sobran puntos al crear personaje (Gracias Tony por ser tan raro)

#Versión 0.5
#Agregada función de guardado y cargado de personaje. 
#Para guardar el personaje, el programa crea un .txt con el nombre y stats del personaje. 
#Para cargar un personaje, el programa lee el .txt y aplica la info de adentro a los stats dentro del juego

import random
import time

class jugador: 
    def __init__(self, nombre, HP, fuerza, defensa):
        self.HP = HP
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa

#Rivales
global PC  
global PC2
global PC3
global PC4 
PC = jugador("Daniel Placeholder", 60, 8, 5)
PC2 = jugador("Juan Normal", 100, 10, 8)
PC3 = jugador("Carlos Testeo", 150, 12, 10)
PC4 = jugador("Ibrahim al-Azar", random.randint(100, 200), random.randint(10,15), random.randint(5, 12))

def main_menu():
    print("Bienvenido a\n")
    time.sleep(0.2)
    print("   ____________\n  / __/ __/ __/\n _\ \/ _// _/  \n/___/_/ /_/    \n")
    time.sleep(0.5)
    print("Creado por Axel Petraglia\nIdea original: Alfredo Suescun\nVersión: Alpha 0.5\n")
    opcion_menu = input("Presione 1 para crear una nueva partida\nPresione 2 para cargar una partida previa\n\n")
    if int(opcion_menu) == 1:
        creacion_pj()
    elif int(opcion_menu) == 2:
        load_file()
    while int(opcion_menu) != 1 and int(opcion_menu) != 2:
        opcion_menu = input("Error de selección.\nPresione 1 para crear una nueva partida\nPresione 2 para cargar una partida previa\n\n")

def creacion_pj():
    puntos = 20
    print("\nBienvenido a la creación de personaje")
    nombre = input("¿Cuál nombre querés darle a tu personaje?: ")
    print("\nTendrá " + str(puntos) + " puntos que podrá asignar a cada habilidad")
    print("\nLas habilidades son:\nHP: Cuántos puntos de vida tenés (el valor que le asigne se multiplicará por 10)\nFuerza: Cuánto daño hacés al golpear\nDefensa: Cuánto daño podes resistir\n")
    time.sleep(1)    

    try:
        HP_pj = (int(input("¿Cuántos puntos quiere asignarle a su HP?: ")) + 1) * 10
    except:
        try:
            HP_pj = (int(input("Por favor usá números, intente de nuevo: ")) + 1) * 10
        except: 
            print("¡Solamente podés usar números! Va a volver al creador de personaje")
            time.sleep(0.6)
            creacion_pj()
    while HP_pj < 0:
        HP_pj = (int(input("Valor inválido, intente de nuevo: ")) + 1) * 10   
    print("Tendrá " + str(HP_pj) + (" puntos de HP"))

    time.sleep(0.6)
    print("\nLe quedan " + str(int(puntos - (int((HP_pj - 1) / 10)))) + " puntos para asignar\n")

    try:
        fuerza_pj = int(input("¿Cuántos puntos quiere asignarle a su Fuerza?: ")) + 1
    except:
        try:
            fuerza_pj = int(input("Por favor use números, intente de nuevo: ")) + 1
        except: 
            print("¡Solamente podés usar números! Va a volver al creador de personaje")
            time.sleep(0.6)
            creacion_pj()
    while fuerza_pj < 0:
        fuerza_pj = int(input("Valor inválido, intente de nuevo: ") + 1)
    print("Tendrá " + str(fuerza_pj) + " puntos de fuerza")

    time.sleep(0.6)
    print("\nLe quedan " + str(int(puntos - (int((HP_pj - 1) / 10) + (fuerza_pj - 1)))) + " puntos para asignar\n")
    try:
        defensa_pj = int(input("¿Cuántos puntos quiere asignarle a su Defensa?: ")) + 1
    except:
        try:
            defensa_pj = int(input("Valor inválido, intente de nuevo: ") + 1)
        except: 
            print("¡Solamente podés usar números! Va a volver al creador de personaje")
            time.sleep(0.6)
            creacion_pj()
    while defensa_pj < 0:
        defensa_pj = int(input("Valor inválido, intente de nuevo: ") + 1)
    print("Tendrá " + str(defensa_pj) + (" puntos de defensa"))
    time.sleep(0.6)
    
    global PJ
    PJ = jugador(nombre, HP_pj, fuerza_pj, defensa_pj) 

    if int(int((HP_pj - 1 ) / 10) + int(fuerza_pj - 1) + int(defensa_pj - 1)) == puntos:
        time.sleep(0.5)
        print("\n¡Su personaje " + nombre + " ha sido creado con éxito!")
        print("\nTu personaje va a tener: \n" + str(HP_pj) + " Puntos de HP\n" + str(fuerza_pj) + " Puntos de Fuerza\n" + str(defensa_pj) + " Puntos de Defensa")
        save_eleccion = input("----------------------------------\n¿Quiere guardar su personaje?:\nPresione Y para guardar\nPresione N para ir directo a elegir su rival\n\n")
        save_eleccion = save_eleccion.lower()
        if save_eleccion == "y":
            save_file()
        elif save_eleccion == "n":
            eleccion()
        while save_eleccion != "y" and save_eleccion != "n":
            save_eleccion = input("Error de selección.\nPresione Y para guardar\nPresione N para ir directo a elegir su rival\n\n")    
        time.sleep(0.5)

    elif int(int((HP_pj - 1 ) / 10) + int(fuerza_pj - 1) + int(defensa_pj - 1)) < puntos:
        time.sleep(0.5)
        print("\nHa utilizado menos de los puntos asignados, ¿Está seguro que quiere continuar?")
        continuar = input("Presione Y para continuar o Presione N para volver a crear su personaje: ")
        continuar = continuar.lower()
        while (continuar != "y" and continuar != "n"):
            print(continuar)
            continuar = input("\nOpción inválida.\nPresione Y para continuar de todos modos o presione N para volver a crear su personaje: ")
            continuar = continuar.lower()
        if continuar == "y":
            save_eleccion = input("----------------------------------\n¿Quiere guardar su personaje?:\nPresione Y para guardar\nPresione N para ir directo a elegir su rival\n\n")
            save_eleccion = save_eleccion.lower()
            if save_eleccion == "y":
                save_file()
            elif save_eleccion == "n":
                eleccion()
            while save_eleccion != "y" and save_eleccion != "n":
                save_eleccion = input("Error de selección.\nPresione Y para guardar\nPresione N para ir directo a elegir su rival\n\n")    
            time.sleep(0.5)
        elif continuar == "n":
            creacion_pj()

    elif int(int((HP_pj - 1 ) / 10) + int(fuerza_pj - 1) + int(defensa_pj - 1)) < 0:
        print("\nHa utilizado más puntos que los que tiene asignados. Intente de nuevo")
        time.sleep(1)
        creacion_pj()

    else:
        time.sleep(1)
        print("\nHa utilizado más puntos que los que tiene asignados. Intente de nuevo")
        time.sleep(1)
        creacion_pj()

def save_file():
    save = open("SaveSFF.txt", "w+")
    save.writelines(str(PJ.nombre) + "\n" + str(PJ.HP) + "\n" + str(PJ.fuerza) + "\n" + str(PJ.defensa))
    time.sleep(0.5)
    save.close()
    print("Su partida ha sido guardada con éxito")
    eleccion()

def load_file():
    load = open("SaveSFF.txt", "r")

    load_nombre = load.readline()
    nombre_cargado = load_nombre.strip()
    
    load_HP = load.readline() 
    HP_cargado = load_HP.strip()    

    load_fuerza = load.readline()
    fuerza_cargado = load_fuerza.strip()

    load_defensa = load.readline()
    defensa_cargado = load_defensa.strip()

    global PJ
    PJ = jugador(nombre_cargado, HP_cargado, fuerza_cargado, defensa_cargado)

    print("\nTu personaje " + PJ.nombre + " tiene: \n" + str(PJ.HP) + " Puntos de HP\n" + str(PJ.fuerza) + " Puntos de Fuerza\n" + str(PJ.defensa) + " Puntos de Defensa")
    time.sleep(0.5)
    load.close()
    print("\nBienvenido de vuelta")
    time.sleep(0.2)
    eleccion()  

def eleccion():
    print("\nPuedes pelear con los siguientes rivales:\nDaniel Placeholder: Presiona 1\nJuan Normal: Presiona 2\nCarlos Testeo: Presiona 3\nIbrahim al-Azar: Presiona 4")
    global rival_elegido
    rival_elegido = input("\n¿Contra qué rival querés enfrentarte?: ")
    pelea()
    
def pelea(): 
    if rival_elegido == "1":
        hp_pc = int(PC.HP)
        fuerzac = int(PC.fuerza)
        defensac = int(PC.defensa)
        nombre_pc = PC.nombre
    elif rival_elegido == "2":
        hp_pc = int(PC2.HP)
        fuerzac = int(PC2.fuerza)
        defensac = int(PC2.defensa)
        nombre_pc = PC2.nombre
    elif rival_elegido == "3":
        hp_pc = int(PC3.HP)
        fuerzac = int(PC3.fuerza)
        defensac = int(PC3.defensa)
        nombre_pc = PC3.nombre
    elif rival_elegido == "4":
        hp_pc = int(PC4.HP)
        fuerzac = int(PC4.fuerza)
        defensac = int(PC4.defensa)
        nombre_pc = PC4.nombre

    hp_pj = int(PJ.HP) 
    fuerzaj = int(PJ.fuerza)
    defensaj = int(PJ.defensa)

    while hp_pc > 0 and hp_pj > 0: 
        if hp_pc == 0 or hp_pj == 0: 
            continue
        print("----------------------------------\n\nTenés " + str(hp_pj) + " puntos de vida.\n" + nombre_pc + " tiene: " + str(hp_pc) + " puntos de vida.\n") # Printea cuánto HP tenes vos y el rival
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
    
        min_dañopc = int(defensaj / 2)
        max_dañopc = defensaj * 2
        rango_dañopc = max(random.randint(min_dañopc, max_dañopc), 0)
        if max_dañopc < 0:
            max_dañopc = 0

        min_dañopj = int(defensac / 2)
        max_dañopj = defensac * 2
        rango_dañopj = max(random.randint(min_dañopj, max_dañopj), 0)

        print("\n" + nombre_pc + " eligió: " + computer + "\n")
        if jugador == computer: 
            print("\n--¡Empate!--") 
        elif (jugador == "piedra"):                  
            if (computer == "papel"):                
                print("\n<<¡Punto para " + nombre_pc + "!>>\n\n¡Te quita " + str(int(2*fuerzac) - rango_dañopj)  + " puntos de vida!") 
                hp_pj = hp_pj - (int(2*fuerzac) - rango_dañopj)                    
            else:
                print("\n||¡Punto para vos!||\n\n¡Le quitas " + str(int(2*fuerzaj) - rango_dañopc) + " puntos de vida!")
                hp_pc = hp_pc - (int(2*fuerzaj) - rango_dañopc)
        elif (jugador == "papel"):
            if (computer == "piedra"):
                print("\n||¡Punto para vos!||\n\n¡Le quitas " + str(int(2*fuerzaj) - rango_dañopc)  + " puntos de vida!")
                hp_pc = hp_pc - (int(2*fuerzaj) - rango_dañopc)
            else:
                print("\n<<¡Punto para " + nombre_pc + "!>>\n\n¡Te quita " + str(int(2*fuerzac) - rango_dañopj)  + " puntos de vida!") 
                hp_pj = hp_pj - (int(2*fuerzac) - rango_dañopj) 
        elif (jugador == "tijera"):
            if (computer == "piedra"):
                print("\n<<¡Punto para " + nombre_pc + "!>>\n\n¡Te quita " + str(int(2*fuerzac) - rango_dañopj)  + " puntos de vida!") 
                hp_pj = hp_pj - (int(2*fuerzac) - rango_dañopj) 
            else:
                print("\n||¡Punto para vos!||\n\n¡Le quitas " + str(int(2*fuerzaj) - rango_dañopc)  + " puntos de vida!")
                hp_pc = hp_pc - (int(2*fuerzaj) - rango_dañopc)
    
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

main_menu()
