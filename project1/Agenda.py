class Agenda(Proceso.Proceso):

    def __init__(self,nombre,tiempo,nombre_contacto,numero):
    	self.id = id
    	self.name = nombre
    	self.time = tiempo
    	self.contact = nombre_contacto
    	self.number = numero

    def getContact(self):
    	return self.contact

    def getNumber(self):
    	return self.number
