# Menu
import ram
import Creacion_archivo

ram = ram()

def subir_archivo():

	nombre_archivo = raw_input("introduzca el nombre del archivo a subir")
	espacio_suficiente, cant_bloques = Creacion_archivo.restriccion_archivo(nombre_archivo):
		ram.agregar_archivo(cant_bloques, nombre_archivo)

def main():
	
	opcion = input("Presione: 1 para subir archivo\n 2 para agregar contacto al disco")
	if opcion == 1:
		subir_archivo()
		