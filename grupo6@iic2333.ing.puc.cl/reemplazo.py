def reemplazar(lista,bloquesFaltantes):

        i = 0
        
        id = []
        contadores = []
        
        while i < len(lista):
                
                if not lista[i][0] in id and lista[i][0] != 0:
                        id.append(lista[i][0])
                        contadores.append(0)
                        
                i = i + 1
                
        i = 0
        
        while i < len(lista):
        
                j = 0
                
                while j < len(id):
                
                        if lista[i][0] == id[j]:
                        
                                contadores[j] = contadores[j] + 1
                                break
                        j = j + 1
                        
                i = i + 1
                
        min = 0
        max = 0
        
        borrar = []
        
        space = 0
        
        while space < bloquesFaltantes and len(contadores) > 0:  
        
                i = 0
                while i < len(contadores):
                
                        if contadores[i] < contadores[min]:
                                min = i
                        if contadores[i] > contadores[max]:
                                max = i
                        i = i + 1
                        
                if space + contadores[min] < bloquesFaltantes:
                        space = space+ contadores[max]
                        borrar.append(id[max])
                        del contadores[max]
                        del id[max]
                        max = 0
                        min = 0
                else:
                        space = space+ contadores[min]
                        borrar.append(id[min])
                        del contadores[min]
                        del id[min]
                        min = 0
                        max = 0
        
        return borrar                                
                                                                                        

									
					
