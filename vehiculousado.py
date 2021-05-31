from vehiculo import vehiculo
from datetime import date
class vehiculoUsado(vehiculo):
    __patente = ''
    __ano = None
    __kilometraje = 0
    __preciofin = 0
    def __init__(self, cantpuert, color, precio, marca, patente, ano, kilometraje):
        super().__init__(cantpuert,color,precio,marca)
        self.__patente = patente
        self.__ano = ano
        self.__kilometraje = kilometraje
        self.__preciofin = super().getPrecio() - (super().getPrecio() * ((date.today().year - self.__ano)/100))
        if self.__kilometraje > 100000:
            self.__preciofin = super().getPrecio() - (super().getPrecio() * 0.02)
    def getPatente(self):
        return self.__patente
    def actPrecio(self):
        self.__preciofin = super().getPrecio() - (super().getPrecio() * ((date.today().year - self.__ano)/100))
        if self.__kilometraje > 100000:
            self.__preciofin = super().getPrecio() - (super().getPrecio() * 0.02)
        return self.__preciofin
    def __str__(self):
        return 'Puertas: %d Color: %s Precio final: %f Marca %s' % (super().getPuertas(), super().getColor(), self.__preciofin, super().getMarca()) 
    def mostrarDatos(self):
        return 'Puertas: %d Color: %s Precio final: %f Marca %s, Patente %s, Año %d, Kilometraje %d, Precio base %d' % (super().getPuertas(), super().getColor(), self.__preciofin, super().getMarca(), self.__patente, self.__ano, self.__kilometraje, super().getPrecio()) 
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    cantpuert=super().getPuertas(),
                                    color=super().getColor(),
                                    precio=super().getPrecio(),
                                    marca=super().getMarca(),
                                    patente = self.__patente,
                                    kilometraje = self.__kilometraje,
                                    ano = self.__ano,
                                )
                )
        return d
