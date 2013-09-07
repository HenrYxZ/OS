# En esta clase se debe poner toda la logica para leer el archivo de entrada
#import Proceso
import string

class Parser:
  
    def __init__ (self,nombre_archivo):
        self.n_archivo = nombre_archivo #Inicializamos la clase con el nombre del archivo que leeremos
  
  
    def Leer_Archivo(self):
        archivo = open(self.n_archivo,"r") #abrimos el archivo que queremos
        
        while True:
            linea = archivo.readline() #leemos las lineas
            if not linea:
                break
            else:
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
                

                #ahora que tenemos todos los atributos, vemos los casos, los cuales son 10


        archivo.close() #Finalmente cerramos el archivo
