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
                indice = linea.find(';') #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                print nombre;
                print indice;
            
            
        archivo.close() #Finalmente cerramos el archivo

Par = Parser("prueba.txt")
Par.Leer_Archivo()
