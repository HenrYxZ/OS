# Menu
from ram import ram
import Creacion_archivo

ram = ram()

def subir_archivo():

	nombre_archivo = raw_input("introduzca el nombre del archivo a subir 	")
	espacio_suficiente, cant_bloques = Creacion_archivo.restriccion_archivo(nombre_archivo)
	if espacio_suficiente:
		ram.agregar_archivo(cant_bloques, nombre_archivo)

def main():
	while(True):
		opcion = input("Presione:\n 1 para subir archivo \n 2 para agregar contacto al disco \n 3 para leer archivo \n 0	para salir \n")
		if opcion == 1:
			subir_archivo()
		else:
			break

if __name__ == "__main__":
    main()
		