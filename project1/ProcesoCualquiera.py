import Proceso

class ProcesoCualquiera(Proceso.Proceso):

	def __init__(self,nombre,fecha,tipo_proceso,prioridad,duracion):
		self.id = id
		self.name = nombre
		self.date = fecha
		self.tipo = tipo_proceso
		self.priority = prioridad
		self.length = duracion

	def getLength(self):
		return self.length
		
