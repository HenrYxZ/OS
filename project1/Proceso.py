class Proceso:

    def __init__(self,id,nombre,fecha,tipo_proceso,prioridad):
        self.id = id
        self.name = nombre
        self.date = fecha
        self.type = tipo_proceso
        self.priority = prioridad
        self.state = "new"

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getType(self):
        return self.type
        
    def getPriority(self):
        return self.priority
        
    def getId(self):
        return self.id

    def getState(self):
        return self.state
        
