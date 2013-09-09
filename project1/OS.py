from Parser import Parser

# ------------- inicio ---------------

nombre_archivo = "example.txt"
parser = Parser(nombre_archivo)
procesos = parser.Leer_Archivo()
procesos.sort(key = lambda x: x.date)
for i in range(len(procesos)):
	print ("Proceso %d fecha %d" % procesos[i].getName(), procesos[i].getDate() )