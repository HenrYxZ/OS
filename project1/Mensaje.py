import Proceso

tiempo_por_caracter = 0.02

class Mensaje(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,numero,texto):
        self.id = id
        self.name = nombre
        self.date = fecha
    	self.type = tipo_proceso
    	self.priority = prioridad
        self.number = numero
        self.text = texto
        # Se resta 1 a len porque se cuenta el caracter de fin de linea
        self.length = tiempo_por_caracter * len(texto)-1

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text

    def getLength(self):
        return self.length

    def run(self):
        texto = ("Proceso %s id=%d corriendo, falta %d" % self.name, self.id, self.length)
        print texto
