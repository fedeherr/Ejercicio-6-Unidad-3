# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:47:46 2020
@author: morte
"""
import json
from pathlib import Path
from lista import Lista
from vehiculo import vehiculo
from vehiculousado import vehiculoUsado
from vehiculonuevo import vehiculoNuevo

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            lis = Lista()
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                vehiculos=d['vehiculos']
                manejador=class_()
                for i in range(len(vehiculos)):
                    dVehiculo=vehiculos[i]
                    class_name=dVehiculo.pop('__class__')
                    class_=eval(class_name)
                    atributos=dVehiculo['__atributos__']
                    unVehiculo=class_(**atributos)
                    lis.agregarVehiculo(unVehiculo)
            return lis    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()            
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)