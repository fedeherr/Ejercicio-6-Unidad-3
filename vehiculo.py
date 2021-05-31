class vehiculo():
    __cantpuert = 0
    __color = ''
    __precio = 0
    __marca = ''
    def __init__(self, cantpuert, color, precio, marca):
        self.__cantpuert = cantpuert
        self.__color = color
        self.__precio = precio
        self.__marca = marca
    def getPrecio(self):
        return(self.__precio)
    def getColor(self):
        return self.__color
    def getMarca(self):
        return self.__marca
    def setMarca(self, marca):
        self.__marca = marca
    def getPuertas(self):
        return self.__cantpuert
    def setPrecio(self, precio):
        self.__precio = precio
        
        