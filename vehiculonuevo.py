from vehiculo import vehiculo
class vehiculoNuevo(vehiculo):
    __version = ''
    __precio = 0.0
    def __init__(self, cantpuert, color, precio, marca, version):
        super().__init__(cantpuert,color,precio,marca)
        self.__version = version
        self.__precio = super().getPrecio() * 1.1
        if (self.__version == 'Full'): self.__precio += super().getPrecio() * 0.02
    def __str__(self):
        return 'Puertas: %d, Color: %s, Precio final: %f, Marca %s,' % (super().getPuertas(), super().getColor(), self.__precio, super().getMarca())
    def mostrarDatos(self):
        return 'Puertas: %d, Color: %s, Precio final: %f, Marca %s, Versión %s, Precio base: %d' % (super().getPuertas(), super().getColor(), self.__precio, super().getMarca(), self.__version, super().getPrecio()) 
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    cantpuert=super().getPuertas(),
                                    color=super().getColor(),
                                    precio=super().getPrecio(),
                                    marca=super().getMarca(),
                                    version = self.__version,
                                )
                )
        return d
    def setMarca(self, marca):
        super().setMarca(marca)