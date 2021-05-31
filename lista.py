from nodo import Nodo
from vehiculo import vehiculo
from vehiculonuevo import vehiculoNuevo
from vehiculousado import vehiculoUsado
from Interface import elementos
from zope.interface import implementer, implements
@implementer(elementos)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __sig=None
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
             self.__actual=self.__comienzo
             self.__indice=0
             raise StopIteration
        else:
             self.__indice+=1
             dato = self.__actual.getDato()
             self.__actual=self.__actual.getSiguiente()
             return dato
    def getSiguiente(self):
        return self.__actual.getSiguiente()
    def agregarVehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def ReemplazarVehiculo(self, vehi, sig):
        nodo = Nodo(vehi)
        nodo.setSiguiente(sig)
        self.__actual=nodo
        self.__comienzo=nodo
    def getActual(self):
        return self.__actual
    def mostrarElemento(self, pos):   
        aux = self.__comienzo
        i = 0
        while i<pos and aux != None:
            aux = aux.getSiguiente()
            i +=1
        if aux == None:
            raise IndexError
        else:
            return aux.getDato()
    def insertarElemento(self, ind, vehiculo):
        if ((ind >= self.__tope) or (ind < 0)): raise IndexError('Indice de la lista fuera de rango')
        aux = self.__comienzo
        encontrado = False
        i = 0
        c = 0
        if (i == ind):
            self.agregarVehiculo(vehiculo)
        else:
            ant = aux
            aux = aux.getSiguiente()
            i += 1
            while ((not encontrado)&(aux != None)):
                if i == ind:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
                    i +=1
            if ((encontrado)&(aux.getSiguiente() != None)):
                viejo = aux.getDato()
                aux.setDato(vehiculo)
                aux = aux.getSiguiente()
                
                viejo2 = aux.getDato()
                aux.setDato(viejo)
                while(aux.getSiguiente() != None):
                        aux = aux.getSiguiente()
                        viejo = aux.getDato()
                        aux.setDato(viejo2)
                        c = 1
                        if (aux.getSiguiente() != None):
                            aux = aux.getSiguiente()
                            viejo2 = aux.getDato()
                            aux.setDato(viejo)
                            c = 0
                if (c == 0):
                    final = Nodo(aux.getDato())
                    aux.setDato(viejo)
                    final.setDato(viejo2)
                else:
                    final = Nodo(aux.getDato())
                    aux.setDato(viejo2)
                    final.setDato(viejo)
                self.__tope+=1
                aux.setSiguiente(final)
            else:
                if(aux.getSiguiente() == None):
                    final = Nodo(aux.getDato())
                    aux.setDato(vehiculo)
                    aux.setSiguiente(final)
                    self.__tope+=1

    def tipoObj(self, ind):
        if ((ind >= self.__tope) or (ind < 0)): raise IndexError('Indice de la lista fuera de rango')
        i = 0
        aux = self.__comienzo
        ant = aux
        while(i != ind):
            aux = aux.getSiguiente()
            ant = aux
            i += 1
        a = (ant.getDato())
        a = str(a.__class__)
        print ("Este objeto es de clase: ", a)

    def modPre(self, patente):
        i = 0
        aux = self.__comienzo
        bandera = False
        while(not bandera):
            ant = aux
            aux = aux.getSiguiente()
            i += 1
            if (isinstance (ant.getDato(), vehiculoUsado)):
                if (ant.getDato().getPatente() == patente):
                    bandera = True
        if bandera:
            nuevopre = int(input("Ingrese el nuevo precio base: "))
            ant.getDato().setPrecio(nuevopre)
            ant.getDato().actPrecio()
    def masEconomico(self):
        minimo = 1000000
        peque = None
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            if (ant.getDato().getPrecio() < minimo):
                minimo = ant.getDato().getPrecio()
                peque = ant.getDato()
        return peque

    def toJSON(self):
        vehi = self.__actual.getDato()
        vehiculoslis = []
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            vehiculoslis.append(ant.getDato().toJSON())
        d = dict(
                __class__=self.__class__.__name__,
                vehiculos=vehiculoslis
                )
        return d

    def mostrarLista(self):
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            print(ant.getDato())

    def setMarca(self, marca):
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            if (isinstance(ant.getDato(),vehiculoNuevo)):
                ant.getDato().setMarca(marca)


        
 
