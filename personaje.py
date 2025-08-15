class Personaje:
    def __init__(self,turno):
        self.nombre =''
        self.turno = turno
        self.posicion = 0

    def setNombre(self):
        nombre=input("Ingrese el nombre de su personaje (o ENTER para finalizar): ").lower()
        self.nombre=nombre
             
    
    def getNombre(self):
        return self.nombre

    def avanzar(self, pasos, tablero):
        self.posicion += pasos
        if self.posicion >= tablero.cant_casillas:
            self.posicion = tablero.cant_casillas
        casilla=tablero.obtener_casilla(self)
        if casilla:
            print(f"El jugador {self.nombre} ha caído en una casilla de tipo [ {casilla.tipo} ]")
            casilla.aplicar_efecto(self,tablero)

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")
