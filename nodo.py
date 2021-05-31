class Nodo:
    __vehiculo=None
    __siguiente=None
    __indice = 0
    def __init__(self, vehiculo):
        self.__vehiculo=vehiculo
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__vehiculo
    def setDato(self, vehiculo):
        self.__vehiculo = vehiculo
    def __str__(self):
        return self.__vehiculo