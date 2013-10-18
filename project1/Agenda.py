import Proceso

class Agenda(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,nombre_contacto,numero):
     self.id = id
     self.name = nombre
     self.date = fecha
     self.type = tipo_proceso
     self.priority = prioridad
     self.contact = nombre_contacto
     self.number = numero
     self.length = 1

    def getContact(self):
     return self.contact

    def getNumber(self):
     return self.number

    def run(self):
        texto = ("Proceso " + self.name +  " corriendo")
        print texto
