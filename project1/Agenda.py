import Proceso

class Agenda(Proceso.Proceso):

    def __init__(self,nombre,fecha,tipo_proceso,prioridad,nombre_contacto,numero):
     self.id = id
     self.name = nombre
     self.date = fecha
     self.tipo = tipo_proceso
     self.priority = prioridad
     self.contact = nombre_contacto
     self.number = numero

    def getContact(self):
     return self.contact

    def getNumber(self):
     return self.number
