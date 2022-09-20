import random
import pandas as pd

class equipo:
    def __init__(self, peso_base, nombre, historial, bonusposteo, peso_rand, peso_cont):
        self.peso_base = peso_base
        self.nombre = nombre
        self.historial = historial
        self.bonusposteo = bonusposteo
        self.peso_rand = peso_rand
        self.peso_cont = peso_cont

#peso_base: el puntaje 1
#historial: equipos más ganadores tienen más chances de seguir siendo buenos (final ganada = 5; final perdida = 3, semifinal = 1)
#bonus por posteo: los que en esa tanda hayan publicado sobre futbol tienen un bonus;
#peso random: A veces un equipo puede tener una generación dorada y ese mundial punchean por encima de su talle
#peso_cont: El continente afecta mucho el resultado de lo paises (Eulasia = 5, Pharos = 4, el resto 0)

def load_file():
    datos = pd.read_excel('GrandPrixExcel.xlsx')
    print(datos)

    global equipo1
    equipo1 = equipo(str("1"), (datos.loc[0][0]), str(datos.loc[0][1]), str(datos.loc[0][2]), random.randint(0, 5), str(datos.loc[0][3]))
    peso_equipo1 = str(int(equipo1.historial) + int(equipo1.bonusposteo) + int(equipo1.peso_rand) + int(equipo1.peso_cont))

    print("\nEquipo: " + equipo1.nombre + "\nHistorial: " + str(equipo1.historial))
    print("Bonus por posteo: " + str(equipo1.bonusposteo) + "\nPeso Random: " + str(equipo1.peso_rand) + "\nBonus continental: " + str(equipo1.peso_cont))
    print("\nPeso total = " + peso_equipo1)

    global equipo2
    equipo2 = equipo(str("1"), (datos.loc[1][0]), str(datos.loc[1][1]), str(datos.loc[1][2]), random.randint(1, 5), str(datos.loc[1][3]))
    peso_equipo2 = str(int(equipo2.historial) + int(equipo2.bonusposteo) + int(equipo2.peso_rand) + int(equipo2.peso_cont))

    print("\nEquipo: " + equipo2.nombre + "\nHistorial: " + str(equipo2.historial))
    print("Bonus por posteo: " + str(equipo2.bonusposteo) + "\nPeso Random: " + str(equipo2.peso_rand) + "\nBonus continental: " + str(equipo2.peso_cont))
    print("\nPeso total = " + peso_equipo2)

#Usamos un excel con los datos que pide la class, y lo sacamos de ahí
#Cada grupo en una sheet de excel

def partidos():
    peso_equipo_a = str(int(equipo1.historial) + int(equipo1.bonusposteo) + int(equipo1.peso_rand) + int(equipo1.peso_cont))
    peso_equipo_b = str(int(equipo2.historial) + int(equipo2.bonusposteo) + int(equipo2.peso_rand) + int(equipo2.peso_cont))
    coeficiente1 = int(peso_equipo_a)/(int(peso_equipo_a)+int(peso_equipo_b))
    coeficiente2 = int(peso_equipo_b)/(int(peso_equipo_b)+int(peso_equipo_a))

    print("\nEl peso de " + equipo1.nombre + " es: " + str(coeficiente1))
    print("El peso de " + equipo2.nombre + " es: " + str(coeficiente2))

    coeficiente_partido = random.uniform(0, 1)
    print("\nCoeficiente de partido: " + str(coeficiente_partido))

    if coeficiente1 > coeficiente2:
        coeficiente_big = coeficiente1
        coeficiente_small = coeficiente2
    else:
        coeficiente_big = coeficiente2
        coeficiente_small = coeficiente1

    c_empate = coeficiente_big - coeficiente_small
    print("\nCoeficiente de empate: " + str(c_empate))

    if c_empate < 0.05:
        print("\n¡Empate!")
    elif coeficiente_partido < coeficiente1:
        print("\nGanó " + equipo1.nombre)
    else:
        print("\nGanó " + equipo2.nombre)

#Tengo que re-escribirlo para que los valores sean elegidos segun el partido que sea

load_file()
partidos()

print("----------------------------------")