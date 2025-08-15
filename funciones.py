from personaje import *
from dado import *
from funciones import *
from tablero_y_casillas import *
from recursos import *
from bot import *

import random

jugadores=[]
tablero=Tablero()
tablero.generar_casillas()

"""NPC: NO PLAYABLE CHARACTER ,o jugador no jugable en español, es una forma de describir aquellos
   personajes que no puedes usar y sirven para rellenar o dar más ambiente en el juego. En el caso
   de este juego de dados los npcs son útiles cuando faltan jugadores x en una partida determinada."""

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def tirar_dado_animado():
    for _ in range(10):
        cara = random.randint(1, 6)
        limpiar_consola()
        print("Rodando el dado...\n")
        for linea in dado_caras[cara]:
            print(linea)
        time.sleep(0.1)
    return cara

def validar_nombre(jugador):
    nombre=jugador.getNombre()
    if nombre.strip()=="":
        if len(jugadores) > 1:
            return True
        else:
            print("> Se requieren al menos dos jugadores.")
            verificacion=input("¿Desea agregar bots para completar? (SI/NO): ").lower()
            if verificacion=="si":
                agregar_bots(jugadores)
            elif verificacion !="si" and verificacion !="no":
                print("Error! Debes ingresar SI o NO.") 
            else:
                if len(jugadores) < 2:
                    print("Error! Deben haber 2 jugadores.\n> Ingrese nuevamente.")
                else:
                    return jugadores,False
    else:
        jugadores.append(jugador)

def agregar_bots(jugadores):
    while True:
        bot=Bot(0)
        print()
        print(f"> Has llamado al {bot.nombre} al juego.")
        print()
        jugadores.append(bot)
        limite=input("Desea agregar otro bot? (SI/NO): ").lower()
        if limite=="si":
            continue
        else:
            return jugadores

def sortear_jugadores():
    print("Fase Previa: Sorteo")
    input("Presione ENTER para iniciar ")
    for jugador in jugadores:
        jugador.turno=tirar_dado_animado()
        print()
        print(f"> El jugador {jugador.nombre} sacó el número {jugador.turno}")
        input("Presione ENTER para continuar ")
        limpiar_consola()
        
    print("=================================")
    print("[ Resultados ]")
    print()
    numeracion=0
    for jugador in jugadores:
        numeracion += 1
        print(f"{numeracion}) El jugador {jugador.nombre} sacó el número {jugador.turno}")
    print("=================================")

def determinar_orden():
    while True:
        sortear_jugadores()
        valor_maximo=max(jugador.turno for jugador in jugadores)
        """recorre la lista jugadores extrayendo el valor del turno de cada uno,
        usa el método max para encontrar el número más alto de los turnos obtenidos"""
        jugadores_con_valor_maximo=[jugador for jugador in jugadores if jugador.turno==valor_maximo]
        """Lista con los jugadores que obtuvieron el valor más alto, 6, en caso de que haya un
        empate o para ubicar al jugador que inicia"""

        if len(jugadores_con_valor_maximo)==1:
            for jugador in jugadores_con_valor_maximo:
                print("================================")
                print()
                print(f"[ El jugador {jugador.nombre} inicia, obtuvo un {jugador.turno} ]")
                print()
                print("================================")
                jugador_inicial=jugadores_con_valor_maximo[0]
                """Se accede al primer elemento de la lista de jugadores con
                   el valor más alto mediante el índice 0"""
                jugadores_restantes=[jugador for jugador in jugadores if jugador != jugador_inicial]
                """Se recorre la lista jugadores guardando a todos, excepto al jugador inicial para
                   evitar duplicaciones"""
                jugadores_ordenados=[jugador_inicial] + jugadores_restantes
                                     #Variable           #Lista
                """Se concatenan las listas colocando al jugador que inicia y
                   luego a los demaás"""
                jugar(jugador,jugadores_ordenados,tablero)
            break
        else:
            print("Hubo un empate entre los jugadores:")
            for jugador in jugadores_con_valor_maximo:
                print(f"> {jugador.nombre} sacó el número {jugador.turno}")
            input("Presione ENTER para repetir el sorteo")
            continue

def ingresar_participantes():
    while True:
        jugador=Personaje(0)
        jugador.setNombre()
        validacion=validar_nombre(jugador)
        if validacion:
            break

def jugar(jugador,jugadores,tablero):
    juego_terminado=False
    while not juego_terminado:
        for jugador in jugadores:
            input(f"\nTurno de [ {jugador.nombre} ]\n> Presiona ENTER para tirar el dado...")
            resultado = tirar_dado_animado()
            print(f"\n{jugador.nombre} sacó un {resultado} 🎲")
            jugador.avanzar(resultado,tablero)
            jugador.mostrar_estado()
            print("=" * 30)
            time.sleep(1.5)

            if jugador.posicion == tablero.cant_casillas:
                print(f"\n🎉 ¡{jugador.nombre} ha ganado!")
                juego_terminado = True
                mostrar(victory)
                print()
                finalizar()

def mostrar(imagen):
    for line in imagen.splitlines():
        print(line)
        time.sleep(0.025)

def finalizar():
    fin=input("Presione ENTER para finalizar")
    exit()

def mostrar_portada(portada):
    mostrar(portada)
    print()
    print("=========================================================")
    print("Juego de azar para toda la familia")
    print("¡El primero en llegar a la casilla 15 será el ganador!")
    print("=========================================================")
    print()
