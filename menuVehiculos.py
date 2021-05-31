# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:49:24 2020
@author: morte
"""
class Menu(object):
    def mostrarMenu(self):
        print('Menú de Opciones: ')
        print('-----------------')
        print('1 - Poner un vehiculo en una posición determinada')
        print('2 - Agregar un vehiculo')
        print('3 - Mostrar qué tipo de objeto se encuentra almacenado en una posición.')
        print('4 - Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.')
        print('5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico')
        print('6 - Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.')
        print('7 - Cargar la lista con los datos del archivo')
        print('8 - Almacenar los datos de la lista en un nuevo archivo vehiculos.json')
        print('9 - Actualizar la marca de todos los autos nuevos')
        print('10 - Salir')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione un número del 1 al 6: '))
            if opcion in [1,2,3,4,5,6,7,8, 9, 10]:
                opcionCorrecta=True
        return opcion        