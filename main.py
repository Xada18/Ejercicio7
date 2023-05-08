from ClaseManejadorViajeros import ManejadorViajeros

if __name__ == '__main__':
    archivo = "viajeros.csv"
    ListaViajeros = ManejadorViajeros()
    ListaViajeros.carga(archivo)

    viajero1 = ListaViajeros.buscarViajero(input("Ingrese un viajero: "))
    if viajero1 == None:
        print("Viajero no encontrado")
    else:
        cantidad = input("Ingrese cantidad de millas: ")
        if int(cantidad) == viajero1:
            print(f"Este viajero tiene {cantidad} millas")
        else: 
            print(f"Este viajero no tiene {cantidad} millas")
    print("")

    viajero2 = ListaViajeros.buscarViajero(input("Ingrese un viajero: "))
    if viajero2 == None:
        print("Viajero no encontrado")
    else:
        cantidad = input("Ingrese cantidad de millas: ")
        if viajero2 == int(cantidad):
            print(f"Este viajero tiene {cantidad} millas")
        else: 
            print(f"Este viajero no tiene {cantidad} millas")
    print("")
    


    viajero = ListaViajeros.buscarViajero(input("Ingrese un numero de viajero: "))
    if viajero == None:
        print("Viajero no encontrado")
    else:
        cantidad = input("Ingrese cantidad de millas recorridas: ")
        viajero = int(cantidad) + viajero
        print(viajero)
    print("")

    otroViajero = ListaViajeros.buscarViajero(input("Ingrese un numero de viajero: "))
    if otroViajero == None:
        print("Viajero no encontrado")
    else:
        cantidad = input("Ingrese cantidad de millas a canjear: ")
        otroViajero =  int(cantidad) - otroViajero
        print(otroViajero)
    print("")