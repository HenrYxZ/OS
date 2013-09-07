import Llamada
import Mensaje

class Historial:

	def __init__(self):
		self.calls = []
		self.mesages = []


	def AgregarLlamada(self, llamada):
		self.calls.append(llamada)

	def AgregarMensaje(self, mensaje):
		self.mesages.append(mensaje)

	def getLlamada(self, indice):
		return self.calls[indice]

	def getMensaje(self, indice):
		return self.mesages[indice]

	def getCantidadLlamadas(self):
		return len(self.calls)

	def getCantidadMensajes(self):
		return len(self.mesages)	
