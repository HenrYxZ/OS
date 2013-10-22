import Proceso

class Llamada(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,numero,duracion):
        self.id = id
        self.name = nombre
        self.date = fecha
    	self.type = tipo_proceso
    	self.priority = prioridad
        self.number = numero
        self.length = duracion

    def getNumber(self):
        return self.number

    def getLength(self):
        return self.length

    def run(self):
        texto = ("Proceso " + self.name +  " corriendo, falta " + str(self.length))
        print texto
