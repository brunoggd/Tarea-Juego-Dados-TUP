import random 
from recursos import *
import time

modo_leyenda=["> En este modo tanto potenciadores como trampas están elevados y mejorados.",
            "> Esto afecta también a la cantidad de casillas totales a las que tienes que llegar para ganar.",
            "> Las casillas totales en este modo son...",
            "[!] [ 999 ] [!] ",
            "> La dificultad de este modo depende pura y exclusivamente de tú suerte y habilidad.",
            "> Disfruta haber activado este modo secreto!",
            "> O no, podés estar 2 horas tranquilamente si te tocan dos trampas legendarias.",
            "> Saludos! :)"]

def mostrar(imagen):
    for line in imagen.splitlines():
        print(line)
        time.sleep(0.025)

class Tablero:
    def __init__(self):
        self.cant_casillas=15
        self.casillas=[]
        self.modo_leyenda=False

    def generar_casillas(self):
        if self.modo_leyenda:
            tipos_posibles=["normal","potenciador legendario","potenciador legendario nivel II","trampa legendaria","trampa legendaria nivel II"]
            self.cant_casillas=999
        else:
            tipos_posibles=["normal","potenciador","potenciador nivel II","trampa","trampa nivel II","legendaria"]
        """La parte de abajo del código está indentada así para generar
           casillas independientemente de si el modo leyenda se activa o no,
           dando la posibilidad de que la lista tipos_posibles tenga los
           tipos de casillas legendarias, o normales, pero siempre genere
           los tipos sin importar si el modo leyenda se activa o no"""
        self.casillas=[]
        for i in range(self.cant_casillas):
            tipo=random.choice(tipos_posibles)
            self.casillas.append(Casilla(tipo))
            """Se guarda un objeto de la clase casilla para luego
            gestionar de qué se trata, si es un potenciador,
            una trampa, o normal."""
    
    def obtener_casilla(self,jugador):
        if jugador.posicion < self.cant_casillas:
            return self.casillas[jugador.posicion]
        else:
            return None

class Casilla:
    def __init__(self,tipo):
        self.tipo=tipo

    def aplicar_efecto(self,jugador,tablero):
        if self.tipo=="potenciador":
            jugador.posicion += 3
            print(f"Potenciador: El jugador {jugador.nombre} avanza 3 casillas.")
            mostrar(potenciador)
        elif self.tipo=="potenciador nivel II":
            jugador.posicion += 5
            print(f"Potenciador nivel II: El jugador {jugador.nombre} avanza 5 casillas.")
            mostrar(potenciador)
        elif self.tipo=="trampa":
            jugador.posicion -= 3
            print(f"Trampa: El jugador {jugador.nombre} retrocede 3 casillas.")
            mostrar(trap_2)
        elif self.tipo=="trampa nivel II":
            jugador.posicion -= 5
            print(f"Trampa nivel II: El jugador {jugador.nombre} retrocede 5 casillas.")
            mostrar(trap_2)
        elif self.tipo=="legendaria" and not tablero.modo_leyenda:
            print(f"El jugador {jugador.nombre} ha activado el modo [ L E Y E N D A ]")
            print()
            print("==========================================================")
            print("[ M O D O - L E Y E N D A ]")
            print()
            for oracion in modo_leyenda:
                print(oracion)
            print("==========================================================")
            tablero.modo_leyenda=True
            tablero.generar_casillas()
        elif self.tipo=="potenciador legendario":
            jugador.posicion += 100
            print(f"Potenciador legendario: El jugador {jugador.nombre} avanza 100 casillas.")
            mostrar(potenciador)
        elif self.tipo=="potenciador legendario nivel II":
            jugador.posicion += 150
            print(f"Potenciador legendario nivel II: El jugador {jugador.nombre} avanza 150 casillas.")
            mostrar(potenciador)
        elif self.tipo=="trampa legendaria":
            jugador.posicion -= 75
            print(f"Trampa: El jugador {jugador.nombre} retrocede 75 casillas.")
            mostrar(trap_3)
        elif self.tipo=="trampa legendaria nivel II":
            jugador.posicion -= 150
            print(f"Trampa nivel II: El jugador {jugador.nombre} retrocede 150 casillas.")
            mostrar(trap_3)   
        else:
            mostrar(normal)
            return jugador.posicion

        if jugador.posicion < 0:
            jugador.posicion=0
            """Por si el jugador retrocede mucho"""

        if jugador.posicion >= tablero.cant_casillas:
            jugador.posicion=tablero.cant_casillas
            """Por si el jugador se excede en cuanto a
               casillas avanzadas."""

"""class Tablero:
    def __init__(self):
        self.casillas_totales=15
        self.tipo_casilla={}
        for i in range(self.casillas_totales):
            if i in [3,6,8,13]:
                self.tipo_casilla[i]="trampa"
            else:
                self.tipo_casilla[i]="normal"

    def activar_efecto(self, jugador):
        tipo=self.tipo_casilla.get(jugador.posicion,"normal") #clave, valor por defecto "normal"
        if tipo == "trampa":
            print(f"[!] {jugador.nombre} ha caído en una {tipo} [!]")
            jugador.posicion -= 5
            if jugador.posicion < 0:
                jugador.posicion=0
        else:
            print(f"> {jugador.nombre} avanza normalmente.")"""


        
