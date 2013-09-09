# Escrito por Hernaldo
# llamadas a paquetes standard
# from multiprocessing import Process
import threading
import time
# llamadas a clases del proyecto
from Cola import Cola
import Memoria

class Scheduler:
	def __init__(self, cola):
		self.queue = cola
		self.process_in_cpu = None
		# Todas las listas siguientes son de threads.
		# esta lista almacenara los procesos de llamadas
		self.llamadas = []
		# esta lista almacenara los procesos de mensajes
		self.mensajes = []
		# esta lista almacenara los demas procesos
		self.otros = []

	def run_in_cpu(self, proceso):
		""" Esta funcion toma un proceso como argumento y lo deja corriendo en 
		la CPU real con la clase Thread """
		self.process_in_cpu = proceso
		proceso.state = "running"
		procesoActivo = threading.Thread(target=proceso.run())
		procesoActivo.start()
		procesoActivo.join()

	def schedule_rr(self, tiempo_rr):
		""" Funcion principal que se ejecutara constantemente y tomara procesos
		de  la Cola y los correra por el tiempo indicado """
		# si llega a este punto es porque el tiempo de round robin terminó
		if self.process_in_cpu != None:	# El proceso ha sido interrumpido
			# Aca se puede mandar el proceso de nuevo a la cola y bajarle el
			# tiempo que necesita para ejecutarse
			self.process_in_cpu.length = process_in_cpu.length - tiempo_rr
			self.process_in_cpu.state = "waiting"
			# Llamado a la funcion guardar que debe estar descrita en el
			# modulo (.py) memoria
			Memoria.guardar(process_in_cpu)
			# Agregar el proceso a una cola en que espere
			if self.process_in_cpu.getType() == "Llamada":
				self.llamadas.append(process_in_cpu)
			elif self.process_in_cpu.getType() == "Mensaje":
				self.mensajes.append(process_in_cpu)
			else 
				self.otros.append(process_in_cpu)
			# queue.push(process_in_cpu)
		proceso = queue.pull()
		run_in_cpu(proceso)

	def seleccionarProceso(self):
		
		if len(self.llamadas) == 0:
			if len(self.mensajes) == 0:
				if len(self.otros) == 0:
					return None
				else:
					a = self.otros[0]
					self.otros[0:0] = []
					return a
			else:
				a = self.mensajes[0]
				self.mensajes[0:0] = []
				return a
		else:
			a = self.llamadas[0]
			self.llamadas[0:0] = []
			return a


