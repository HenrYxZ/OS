import os
import Inodo
from reemplazo import reemplazar
from disco import Disco

class ram():

	def __init__(self):
		## VER SI NECESITO CONSTRUCTOR
		self.bloques_memoria = [] ##arreglo que posee el numero de archivo i
		## si el bloque esta ocupado por el archivo i y 0 si no
		self.espacios_libres = 20 #al principiio todos los espacios estaran vacios
		self.cantidad_archivos = 0
		self.nombres_archivos = []
		self.nombres_archivos.append(None) ## LOS NOMBRES VAN DEL INDICE 1 EN ADELANTE
		self.Inodos = []   
		self.disc = Disco()
		for x in xrange(0,20):
			self.bloques_memoria.append([0, 0])
	



	def agregar_archivo(self,cant_bloques, nombre_archivo):
		## recibo la cantidad de bloques que utilizare de la ram y el archivo que deseo guardar
		bloques = [] ## variable que guardara cada bloque de 1024 bytes (a excepcion del ultimo)
		self.nombres_archivos.append(nombre_archivo)
		self.cantidad_archivos += 1 

		posicion_bloques_en_RAM = []

		f = open(nombre_archivo) # abrimos para leer el archivo falta poner DIRECCION

		for x in xrange(0, cant_bloques):
			if x < cant_bloques - 1:
				bloques.insert(x, f.read(1024))
			else:
				bloques.insert(x, f.read(os.path.getsize(nombre_archivo) - 1024*(cant_bloques-1))) ## verificar que la resta sea la correcta
				## leo y guardo en los bloques

		contador_bloques = 0  ## contador que me indica que pedazo de archivo cortado voy copiando

		indice_archivo = self.cantidad_archivos
		
		inode = Inodo(nombre_archivo,indice_archivo)
		##ACA deberia obtener el indice_actual de la clase disco y segun los bloques que necesito
		## poner las direcciones en posicion actual + cant de bloques
		posicion_cabezal_directo = self.disc.getPosActual()
		for k in range(4,4+cant_bloques):
			inode.estructura.insert(k,posicion_cabezal_directo)
			posicion_cabezal_directo += 1
		self.Inodos.append(inode)


		bloques_copiados = 0  #cantidad de pedazos del archivo que ya he copiado


		if self.espacios_libres < cant_bloques:
			##aca va el metodo donde pido espacios y me devuelve un arreglo con los espacios que debo sacar
			reemplazados = reemplazar(self.bloques_memoria,cant_bloques-self.espacios_libres)	
			##obtengo los id de los bloques que reemplazare
			print reemplazados

			for i in range(0,20):
				if self.bloques_memoria[i][0] in reemplazados:
					self.bloques_memoria.insert(i ,[0, 0]) #reemplazo por vacio los bloques con indices devueltos
					print "adentro"


			for j in range(0,20):
				if self.bloques_memoria[j][0] == 0 and bloques_copiados < cant_bloques:
					self.bloques_memoria.insert(j , [indice_archivo, contador_bloques]) #guardo indice, y offset de pedazo de archivo
					posicion_bloques_en_RAM.append(i)
					bloque_abierto_ram = open("ram/"+str(j)+".txt","w") #abro el archivo que quiero

					bloque_abierto_ram.write(bloques[contador_bloques]) ##escribo el pedazo de archivo que quiero escribir

					bloques_copiados += 1
					bloque_abierto_ram.close()
					contador_bloques += 1
					self.espacios_libres -= 1
					##FALTA RETORNAR LOS ARCHIVOS A ALEJANDRO PARA ESCRIBIRLOS EN DISCO
				

				elif bloques_copiados >= cant_bloques: #si ya copie todo, salgo del for
					break
				


		else:
			for x in range(0,20):
				if self.bloques_memoria[x][0] == 0 and bloques_copiados < cant_bloques:
					self.bloques_memoria.insert(x , [indice_archivo, contador_bloques]) #guardo indice, y offset de pedazo de archivo
					posicion_bloques_en_RAM.append(x)
					bloque_abierto_ram = open("ram/"+str(x)+".txt","w") #abro el archivo que quiero

					bloque_abierto_ram.write(bloques[contador_bloques]) ##escribo el pedazo de archivo que quiero escribir

					bloques_copiados += 1
					bloque_abierto_ram.close()
					contador_bloques += 1
					self.espacios_libres -= 1
					##FALTA RETORNAR LOS ARCHIVOS A ALEJANDRO PARA ESCRIBIRLOS EN DISCO

				elif bloques_copiados >= cant_bloques:
					break

		f.close()
		return posicion_bloques_en_RAM


	def leer_archivo(self,name_archivo):


		if name_archivo in nombres_archivos:
			posicion = nombres_archivo.index(name_archivo) #obtenemos el id que representa a ese archivo
			#AHORA debo verificar que el archivo este en la RAM, sino lo iremos a buscar
			encontrado = False

			for x in xrange(0,20):
				if posicion in bloques_memoria[x]: #si esta dentro de la memoria RAM, sino, busco el disco y copio a RAM
					encontrado = True

			if encontrado == True:
				##aca debo obtener todo los bloques tales que bloques_memoria[x,0] == posicion.
				partes = []
				for i in range(0,20):
					if bloques_memoria[i][0] == posicion:
						partes.append([i,bloques_memoria[i][1]])
				##Al obtener todos los bloques, debo ordenarlos segun el segundo parametros de bloques_memoria
				
				partes = sorted(partes, key = lambda student: student[1]) ##metodo para ordenar

				# es decir segun bloques_memoria[x,1]... luego los imprimo en consola y los muestro
				## Ahora simplemente leo los archivo de nombre (i).txt de partes y los imprimo

				for j in range(0,len(partes)):
					f = open("ram/"+partes[j][0]+".txt")
					dato = f.read()
					print dato
					f.close()

			##else:
				#si no lo encuentro, el disco los debe copiar en la RAM y luego debo leerlos
				##FALTA METODO DE DISCO DURO





