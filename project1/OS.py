import Parser
import Scheduler
import time

def partition(myList, start, end):
    pivot = myList[start].getDate()
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left].getDate() <= pivot:
            left = left + 1
        while myList[right].getDate() >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right                               # Return the split point


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList




# ------------- inicio ---------------

nombre_archivo = "example.txt"
parser = Parser.Parser(nombre_archivo)
procesos = parser.Leer_Archivo()
quicksort(procesos,0,len(procesos)-1)
#procesos.sort(key = lambda x: x.date)

tactual = 0
agendador = Scheduler.Scheduler([])

#for i in range(len(procesos)):
#	print ("Proceso " + str(procesos[i].getName()) + " fecha " +  str(procesos[i].getDate()) )

while True:
	if(len(procesos)>0):
		if(tactual == procesos[0].getDate()):
			newproc = procesos.pop(0)
			print ("Proceso " + str(newproc.getName()) + " fecha " +  str(newproc.getDate()) )
			agendador.nuevoProceso(newproc)
			time.sleep(1)
	tactual = tactual+1

	if(tactual == 45):
		break


		

