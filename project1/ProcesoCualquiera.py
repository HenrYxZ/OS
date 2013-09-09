import Proceso

class ProcesoCualquiera(Proceso.Proceso):

	def __init__(self,nombre,fecha,tipo_proceso,prioridad,duracion):
		self.id = id
		self.name = nombre
		self.date = fecha
		self.type = tipo_proceso
		self.priority = prioridad
		self.length = duracion
		self.state = "new"

	def getLength(self):
		return self.length

	def run(self):
		print ("Proceso %s id=%d corriendo, falta %d" % self.name, self.id,self.length)
