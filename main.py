from vehiculonuevo import vehiculoNuevo
from vehiculousado import vehiculoUsado
from ObjectEncoder import ObjectEncoder
from menuVehiculos import Menu
from lista import Lista
if __name__=='__main__':
    jsonF=ObjectEncoder()
    vehiculos = Lista()
    bandera=True
    marcavehinuevo = "MarcaVehiculoNuevo"
    print ("Iniciando sesión, el programa se inicia sin ningun vehiculo almacenado, algunas funciones de este programa necesitara que cree vehiculos o los cargue del archivo antes de ejecutarlas, si no, dará error.")
    while bandera:
        menu=Menu()
        vehi = 'xd'
        opcion=menu.mostrarMenu()
        if opcion==1:
            print('Creando un nuevo vehiculo')
            cantpuert=int(input('Cantidad de puertas: '))
            color=(input('Color: '))
            precio = int(input('Precio base:'))
            est = input("Ingrese si es 'Nuevo' o 'Viejo': ")
            if (est == 'Nuevo'):
                ver = input("Ingrese la version (Base o Full): ")
                if ((ver == 'Base') or (ver == 'Full')):
                    marca = marcavehinuevo
                    vehi = vehiculoNuevo(cantpuert, color, precio, marca, ver)
                else: print("Ingresó una version incorrecta")
            if (est == 'Viejo'):
                patente = input("Ingrese la patente: ")
                ano = int(input("Ingrese el año: "))
                marca = input("Ingrese la marca:")
                kilometraje = int(input("Ingrese el kilometraje: "))
                vehi = vehiculoUsado(cantpuert, color, precio, marca, patente, ano, kilometraje)
            if (vehi != 'xd'):
                indi = int(input("Ingrese la posición donde desea insertar el vehiculo: "))
                vehiculos.insertarElemento(indi, vehi)
                print("Se insertó el vehiculo")
            else: print("Ingreso un vehiculo incorrecto")
        else:
            if opcion==2:
                print('Creando un nuevo vehiculo')
                cantpuert=int(input('Cantidad de puertas: '))
                color=(input('Color: '))
                precio = int(input('Precio base:'))
                est = input("Ingrese si es 'Nuevo' o 'Viejo': ")
                if (est == 'Nuevo'):
                    ver = input("Ingrese la version: ")
                    marca = marcavehinuevo
                    vehi = vehiculoNuevo(cantpuert, color, precio, marca, ver)
                if (est == 'Viejo'):
                    patente = input("Ingrese la patente: ")
                    ano = int(input("Ingrese el año: "))
                    marca = input('Marca: ')
                    kilometraje = int(input("Ingrese el kilometraje: "))
                    vehi = vehiculoUsado(cantpuert, color, precio, marca, patente, ano, kilometraje)
                if (vehi != 'xd'):
                    vehiculos.agregarVehiculo(vehi)
                    print ("Se agregó el vehiculo")
                else: print("Tipo de vehiculo incorrecto")
            else:
                if opcion==8:
                    d=vehiculos.toJSON()
                    jsonF.guardarJSONArchivo(d,'vehiculos.json')
                    print ("Se guardó el archivo")
                else:
                    if opcion==7:
                        diccionario=jsonF.leerJSONArchivo('vehiculos.json')
                        vehiculos=jsonF.decodificarDiccionario(diccionario)
                        print ("Se leyó el archivo")
                    else:
                        if opcion==6:
                            vehiculos.mostrarLista()
                        else:
                            if opcion == 3:
                                ind = int(input("Ingrese el numero de indice a comprobar objeto: "))
                                vehiculos.tipoObj(ind)
                            else:
                                if opcion == 4:
                                    paten = input("Ingrese la patente del vehiculo a modificar precio: ")
                                    vehiculos.modPre(paten)
                                    print ("Se modifico el precio")
                                else:
                                    if opcion == 5:
                                        masec = vehiculos.masEconomico()
                                        print (masec.mostrarDatos())
                                    else:
                                        if opcion == 9:
                                            marcavehinuevo = input("Ingrese la nueva marca de los vehiculos nuevos")
                                            vehiculos.setMarca(marcavehinuevo)
                                            print ("Se actualizó la marca")
                                        else:
                                            if opcion == 10:
                                                bandera=False
                                                print('Ha seleccionado salir, hasta la vuelta')