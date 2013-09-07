# En esta clase se debe poner toda la logica para leer el archivo de entrada
import Proceso
import string

class Parser:
  
    def __init__ (self,nombre_archivo):
        self.n_archivo = nombre_archivo #Inicializamos la clase con el nombre del archivo que leeremos
  
  
    def Leer_Archivo(self):
        archivo = open(self.n_archivo,"r") #abrimos el archivo que queremos
        
        while True:
            linea = f.readline() #leemos las lineas
            if not linea: 
                break
            else:
                    """ Acá debe ir el método que ejecutará la inicialización dependiendo del tipo de proceso, etc.
                    Son 5 los atributos que nos importan, los cuales son: Nombre_Proceso, Fecha_Ejecución, Tipo_Proceso, 
                    Prioridad_Base y [Opciones]"""
                indice = linea.find(",") #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                
                    
            
            
            
            
            
            
            f.close() #Finalmente cerramos el archivo
    
  
