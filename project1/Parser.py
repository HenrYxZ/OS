# En esta clase se debe poner toda la logica para leer el archivo de entrada
import Proceso
import ProcesoCualquiera
import Agenda
import Cola
import Historial
import Llamada
import Memoria
import Mensaje
import string

class Parser:
  
    def __init__ (self,nombre_archivo):
        self.n_archivo = nombre_archivo #Inicializamos la clase con el nombre del archivo que leeremos
  
  
    def Leer_Archivo(self):
        archivo = open(self.n_archivo,"r") #abrimos el archivo que queremos
        
        #ACA CREO LA COLA.... cola_mnivel = Cola(.........)
        lista = []

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

                #ahora que tenemos todos los atributos, vemos los casos

                if tipo_proceso == 1 or tipo_proceso == 2:

                    proceso_retornado = llamadas(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)
                    

                elif tipo_proceso == 3 or tipo_proceso == 4:

                    proceso_retornado = mensajes(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)

                elif tipo_proceso == 5:

                    proceso_retornado = add_contact(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)

                else:
                    proceso_retornado = procesos_cualquiera(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)
                lista.append(proceso_retornado)

        archivo.close() #Finalmente cerramos el archivo
        return lista



    def llamadas(self,n,f,t,pri,op):
        #Metodo para inicializar recepcion y envio de llamadas

        index = op.find(';')

        #obtenemos los parametros
        num_telefono = op[0:index]
        t_ejec = op[index+1:]
        
        proceso_realizado = Llamada.Llamada(n,f,t,pri,num_telefono,t_ejec)

        return proceso_realizado

    def mensajes(self,n,f,t,pri,op):
        #Metodo para incializar recepcion y envio de mensajes

        index = op.find(';')

        #obtenemos los parametros
        receptor = op[0:index]
        texto_enviado = op[index+1:]

        proceso_realizado = Mensaje.Mensaje(n,f,t,pri,receptor,texto_enviado)
        
        return proceso_realizado

    def add_contact(self,n,f,t,pri,op):
        #metodo para agregar un contacto

        index = op.find(';')

        #obtenemos los parametros
        nombre_agregado = op[0:index]
        numero_agregado = op[index+1:]
        #FALTA AGREGAR ESTOS PARAMETROS A LOS PROCESOS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

        proceso_realizado = Agenda.Agenda(n,f,t,pri,nombre_agregado,numero_agregado)

        return proceso_realizado 

    def procesos_cualquiera(self,n,f,t,pri,tiempo_duracion):
        #Este metodo inicializa los tipos de proceso 6,7,8,9 y 10

        #if t == 6:
        #   proceso_realizado = ProcesoCualquiera(n,f,t,pri,tiempo_duracion)

        #elif t == 7:

        #elif t == 8:

        #elif t == 9:

        #elif t == 10:

        proceso_realizado = ProcesoCualquiera.ProcesoCualquiera(n,f,t,pri,tiempo_duracion)
        return proceso_realizado

