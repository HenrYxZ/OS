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

	def run_in_cpu(self, proceso):
		""" Esta funcion toma un proceso como argumento y lo deja corriendo en 
		la CPU real con la clase Thread """
		process_in_cpu = proceso
		proceso.state = "running"
		procesoActivo = threading.Thread(target=proceso.run())
		procesoActivo.start()
		procesoActivo.join()

	def schedule_rr(self, tiempo_rr):
		""" Funcion principal que se ejecutara constantemente y tomara procesos
		de  la Cola y los correra por el tiempo indicado """
		while(True):
			# si llega a este punto es porque el tiempo de round robin terminó
			if process_in_cpu != None:	# El proceso ha sido interrumpido
				# Aca se puede mandar el proceso de nuevo a la cola y bajarle el
				# tiempo que necesita para ejecutarse
				process_in_cpu.length = process_in_cpu.length - tiempo_rr
				process_in_cpu.state = "waiting"
				# Llamado a la funcion guardar que debe estar descrita en el
				# modulo (.py) memoria
				Memoria.guardar(process_in_cpu)
				queue.push(process_in_cpu)
			proceso = queue.pull()
			run_in_cpu(proceso)
			time.sleep(proceso.getLength())


