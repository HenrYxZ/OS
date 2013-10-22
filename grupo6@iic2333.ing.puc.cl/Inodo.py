import os

class Inodo():
	
	def __init__(self,name_archivo, id):
		self.estructura = []
		self.estructura.insert(0,name_archivo)
		self.estructura.insert(1,os.path.getsize(name_archivo))
		self.estructura.insert(2,os.path.abspath(name_archivo))
		self.estructura.insert(3,id)

		"""
		Estructura del i nodo

		[0]: nombre nombre del archivo 
		[1]: tamano del archivo 
		[2]: ubicacion
		[3]: id 
		[4]: bloque directo
		[5]: bloque directo
		[6]: bloque directo
		[7]: bloque directo
		[8]: bloque directo
		[9]: bloque directo
		[10]: bloque directo
		[11]: bloque directo
		[12]: bloque directo
		[13]: bloque directo
		"""



	
