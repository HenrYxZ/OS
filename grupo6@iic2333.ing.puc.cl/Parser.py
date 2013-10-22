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
                indice = linea.find(';') #Obtenemos el indice de la primera coma
                nombre = linea[0:indice] #Nombre del proceso
                
                linea = linea[indice+1:] #Actualizamos la linea
                #obtendremos ahora la fecha de ejecucion
                indice = linea.find(';')
                fecha_ejec = int(linea[0:indice])

                linea = linea[indice+1:] #Actualizamos la linea
                #obtendremos ahora el tipo de proceso
                indice = linea.find(';')
                tipo_proceso = int(linea[0:indice])
            
                linea = linea[indice+1:] #Actualizamos la linea
                #obtendremos ahora la prioridad base
                indice = linea.find(';')
                prioridad_base = int(linea[0:indice])
            
                opciones = linea[indice+1:] #Obtenemos las opciones

                #ahora que tenemos todos los atributos, vemos los casos

                if tipo_proceso == 1 or tipo_proceso == 2:

                    proceso_retornado = self.llamadas(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)
                    

                elif tipo_proceso == 3 or tipo_proceso == 4:

                    proceso_retornado = self.mensajes(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)

                elif tipo_proceso == 5:

                    proceso_retornado = self.add_contact(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)

                else:
                    proceso_retornado = self.procesos_cualquiera(nombre,fecha_ejec,tipo_proceso,prioridad_base,opciones)
                    #ACA agrego el proceso a la COLA del modo....   cola_mnivel.push(proceso_retornado)
                lista.append(proceso_retornado)

        archivo.close() #Finalmente cerramos el archivo
        return lista



    def llamadas(self,n,f,t,pri,op):
        #Metodo para inicializar recepcion y envio de llamadas

        index = op.find(';')

        #obtenemos los parametros
        num_telefono = op[0:index]
        t_ejec = int(op[index+1:])
        
        proceso_realizado = Llamada.Llamada(n,f,t,pri,num_telefono,t_ejec)

        return proceso_realizado

    def mensajes(self,n,f,t,pri,op):
        #Metodo para incializar recepcion y envio de mensajes

        index = op.find(';')

        #obtenemos los parametros
        receptor = op[0:index]
        texto_enviado = op[index+1:]

        proceso_realizado = Mensaje.Mensaje(n,f,t,pri,receptor,texto_enviado)
        print "tiempo_duracion mensaje" + str(proceso_realizado.getLength())
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
        proceso_realizado = ProcesoCualquiera.ProcesoCualquiera(n,f,t,pri, int(tiempo_duracion))
        print "tiempo_duracion" + tiempo_duracion + "num"
        return proceso_realizado

