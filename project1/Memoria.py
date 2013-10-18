# En este archivo se debe guardar el codigo que permita simular la memoria del 
# telefono guardando la informacion, por ejemplo de procesos, mensajes u otra 
# cosa, en archivos

import Proceso
import os.path
import Llamada
import Agenda
import Mensaje
class Memoria:
	
	def __init__(self):
		self.archivos = []
	
	def grabar_proceso(self,nombre,fecha,tipo,prioridad,opciones): #opciones hay que entregarlas unidas por un ; como un string
	
		nombre_creado = nombre + str(fecha) #para poder diferenciarlo... puede existir dos con el mismo nombre pero no mismo nombre y fecha
		#if os.path.exists(archivo):#si el archivo existe, tenemos que sobreescribirlo
		#	os.remove(nombre_creado) # lo borro y lo creo denuevo... no se como borrar todo su contenido, no lo pude encontrar
		
		archivo = open(nombre_creado,'w')#creo el archivo, si ya existe simplemente lo sobreescribo!
		archivo.write(str(nombre)+","+str(fecha)+","+str(tipo)+","+str(prioridad)+","+str(opciones))
		archivo.close()
	
	def grabar_proceso_cualquiera(self,nombre,fecha,tipo,prioridad,tiempo): #opciones es el tiempo de duracion
		nombre_creado = nombre + str(fecha)
		archivo = open(nombre_creado,'w')#creo el archivo, si ya existe simplemente lo sobreescribo!
		archivo.write(str(nombre)+","+str(fecha)+","+str(tipo)+","+str(prioridad)+","+str(opciones))
		archivo.close()
	
	def obtener_llamada(self,nombre_archivo):
		archivo = open(nombre_creado,'r')
		linea = archivo.readline()
		indice = linea.find(',') #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la fecha de ejecucion
                indice = linea.find(',')
                fecha_ejec = linea[0:indice]

                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora el tipo de proceso
                indice = linea.find(',')
                tipo_proceso = linea[0:indice]
            
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la prioridad base
                indice = linea.find(',')
                prioridad_base = linea[0:indice]
            
                opciones = linea[indice+1:] #Obtenemos las opciones
		
                dex = opciones.find(';')

        #obtenemos los parametros
                num_telefono = opciones[0:index]
                t_ejec = opciones[index+1:]
		
		llam = Llamada.Llamada(nombre,fecha_ejec,tipo_proceso,prioridad_base,num_telefono,t_ejec)
		archivo.close()
		return llam
		
	def obtener_mensaje(self,nombre_archivo):
		archivo = open(nombre_creado,'r')
		linea = archivo.readline()
		indice = linea.find(',') #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la fecha de ejecucion
                indice = linea.find(',')
                fecha_ejec = linea[0:indice]

                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora el tipo de proceso
                indice = linea.find(',')
                tipo_proceso = linea[0:indice]
            
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la prioridad base
                indice = linea.find(',')
                prioridad_base = linea[0:indice]
            
                opciones = linea[indice+1:] #Obtenemos las opciones

	        index = opciones.find(';')

        #obtenemos los parametros
                receptor = opciones[0:index]
                texto_enviado = opciones[index+1:]
		men = Mensaje.Mensaje(nombre,fecha_ejec,tipo_proceso,prioridad_base,receptor,texto_enviado)
                archivo.close()
		return men
		
	def obtener_contacto(self,nombre_archivo):
		archivo = open(nombre_creado,'r')
		linea = archivo.readline()
		indice = linea.find(',') #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la fecha de ejecucion
                indice = linea.find(',')
                fecha_ejec = linea[0:indice]

                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora el tipo de proceso
                indice = linea.find(',')
                tipo_proceso = linea[0:indice]
            
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la prioridad base
                indice = linea.find(',')
                prioridad_base = linea[0:indice]
            
                opciones = linea[indice+1:] #Obtenemos las opciones

		index = opciones.find(';')
	
		nombre_agregado = opciones[0:index]
                numero_agregado = opciones[index+1:]

                cont = Agenda.Agenda(nombre,fecha_ejec,tipo_proceso,prioridad_base,nombre_agregado,numero_agregado)
		archivo.close()
		return cont
	
	
	def obtener_otro(self,nombre_archivo):
		archivo = open(nombre_creado,'r')
		linea = archivo.readline()
		indice = linea.find(',') #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la fecha de ejecucion
                indice = linea.find(',')
                fecha_ejec = linea[0:indice]

                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora el tipo de proceso
                indice = linea.find(',')
                tipo_proceso = linea[0:indice]
            
                linea = linea[indice+1:] #Actualizamos la linea
        #obtendremos ahora la prioridad base
                indice = linea.find(',')
                prioridad_base = linea[0:indice]
            
                opciones = linea[indice+1:] #Obtenemos las opciones

		
		otro_pro = ProcesoCualquiera.ProcesoCualquiera(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
		archivo.close()
		return otro_pro
