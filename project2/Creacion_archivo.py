class Creacion_archivo(object):


	def __init__(self):
		



	def restriccion_archivo(archivo_entregado):
		if os.path.getsize(archivo_entregado) > 1024*10: 
			print "El archivo supera el tamaño maximo de procesamiento"
			return False
		elif :  ## si no hay memoria en el disco, tambien debemos retornar false
		else: 
			numero_bloques = (os.path.getsize(archivo_entregado)/1024) + 1

			##Tiramos el archivo a la ram haciendo os.path.getsize(archivo_entregado)/1024 para obtener
			## el numero de bloques aproximando hacia arriba! 

			##metemos bloques a ram

			return True




