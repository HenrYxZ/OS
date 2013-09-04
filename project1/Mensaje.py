import Proceso

class Mensaje(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,numero,texto):
        self.id = id
        self.name = nombre
        self.date = fecha
    	self.tipo = tipo_proceso
    	self.priority = prioridad
        self.number = numero
        self.text = texto

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text
