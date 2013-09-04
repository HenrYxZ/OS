class Proceso:

    def __init__(self,id,nombre,fecha,tipo_proceso,prioridad):
        self.id = id
        self.name = nombre
        self.date = fecha
        self.tipo = tipo_proceso
        self.priority = prioridad

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getTipo(self):
        return self.tipo
        
    def getPriotiry(self):
        return self.priority
        
    def getId(self):
        return self.id
        
