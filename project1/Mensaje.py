import Proceso

class Mensaje(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,numero,texto):
        self.id = id
        self.name = nombre
        self.date = fecha
    	self.type = tipo_proceso
    	self.priority = prioridad
        self.number = numero
        self.text = texto

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text

    def run(self):
        texto = ("Proceso %s id=%d corriendo, falta %d" % self.name, self.id,self.length)
        print texto
