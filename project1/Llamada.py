import Proceso

class Llamada(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,numero,duracion):
        self.id = id
        self.name = nombre
        self.date = fecha
    	self.tipo = tipo_proceso
    	self.priority = prioridad
        self.number = numero
        self.length = duracion

    def getNumber(self):
        return self.number

    def getLength(self):
        return self.length

    def run(self):
        texto = ("Proceso %s id=%d corriendo, falta %d" % self.name, self.id,self.length)
        print texto
