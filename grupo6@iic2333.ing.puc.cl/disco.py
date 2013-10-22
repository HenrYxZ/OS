import os

class Disco():

	def __init__(self):
		self.posicion_actual = 0
		espacio_disponible = 800*512
		bloques_disco = []
		for x in xrange(0,800):
			bloques_disco.append(0)
			

	def Agregar_Bloques(self, nombres_BloquesRam):
		for name in nombres_BloquesRam:
			archivo_ram = open("ram/" + str(name) + ".txt","r")
			linea = archivo_ram.read() #leemos las lineas
			
			tamano_archivo = os.path.getsize("ram/" + str(name) + ".txt")
			if(tamano_archivo > 512):    #ocupamos 2 bloques
				bloque1 = linea[0:511]
				bloque2 = linea[512:tamano_archivo]
				bloques_disco[self.posicion_actual] = 1  #Marcamos los bloques a utilizar
				bloques_disco[self.posicion_actual+1] = 1
				archivo1 = open("disco/" +str(self.posicion_actual) + ".txt", "w")
				archivo1.write(bloque1)   #Escribimos el bloque 
				archivo1.close()
				archivo2 = open("disco/" +str(self.posicion_actual+1) + ".txt", "w")
				archivo2.write(bloque2)
				archivo2.close()
				self.posicion_actual = self.posicion_actual+2
				espacio_disponible = espacio_disponible - 2*512

			else:		#ocupamos solo 1 bloque
				bloque1 = linea[0:tamano_archivo]
				bloques_disco[self.posicion_actual]=1  #marcamos el bloque
				archivo1 = open("disco/" +str(self.posicion_actual) + ".txt", "w")
				archivo1.write(bloque1)
				archivo1.close()
				self.posicion_actual = self.posicion_actual + 1
				espacio_disponible = espacio_disponible - 512


	def Leer_Bloques(self, posicion_inicial, tamano_archivo):
		
		datosArchivo = ""
		nro_bloques_ram = 0
		nro_bloques_disco = 0
		bloques_ram = [] #arreglo a retornar

		if tamano_archivo%1024 > 0: #cantidad de bloques de ram
			nro_bloques_ram = tamano_archivo/1024 + 1
		else:
			nro_bloques_ram = tamano_archivo/1024	
		
		if tamano_archivo%512 > 0:  #cantidad de bloques de disco
			nro_bloques_disco = tamano_archivo/512 + 1
		else:
			nro_bloques_disco = tamano_archivo/512

		#Leemos los datos del archivo y los almacenamos en string temporal datosArchivo
		for i in range(posicion_inicial, nro_bloques_disco + 1):
			archivo_disco = open("disco/" + str(i) + ".txt","r")
			linea = archivo_disco.read()
			datosArchivo = datosArchivo + linea
			archivo_disco.close()

		#Dividimos el string datosArchivo en los bloques de ram retornar
		if nro_bloques_ram>1:
			for i in range(0, nro_bloques_ram-1):
				data = datosArchivo[0:1023]
				datosArchivo = datosArchivo[1024:]
				bloques_ram = bloques_ram + [data]
		bloques_ram = bloques_ram + [datosArchivo] #agrega el ultimo bloque
		return bloques_ram



	def getPosActual(self):
		return self.posicion_actual


	def getEspacioDisponible(self):
		return self.espacio_disponible
