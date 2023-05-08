from claseViajero import ViajeroFrecuente
import csv

class ManejadorViajeros:
    __viajeros = []
    
    def __init__ (self):
        self.__viajeros = []
        
    def carga(self, file):
        archivo = open(file, "r")
        lector = csv.reader(archivo, delimiter=",")
        
        for datos in lector:
            viajero = ViajeroFrecuente(datos[0], datos[1], datos[2], datos[3], datos[4])
            self.__viajeros.append(viajero)
        
    def buscarViajero(self, numero):
        viajero = None
        i = 0
        while viajero == None and i < len(self.__viajeros):
            if numero == self.__viajeros[i].getNumero():
                viajero = self.__viajeros[i]
            i += 1
        
        return viajero
    
    def mayorCantidadMillas(self):
        mayor = self.__viajeros[0]

        for viajero in self.__viajeros:
            if viajero > mayor:
                mayor = viajero

        return mayor