
class ViajeroFrecuente:
    __num_viajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    
    def __init__(self, numero, dni, nombre, apellido, millas):
        self.__num_viajero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = int(millas)

    def getNumero(self):
        return self.__num_viajero
    
    def __str__(self):
        return f"{self.__num_viajero}, {self.__dni}, {self.__nombre} {self.__apellido}, {self.__millas_acum}"
        
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, millas_recorridas):
        self.__millas_acum += millas_recorridas
        return self.cantidadTotalMillas()
    
    def canjearMillas(self, millas_canje):
        if millas_canje > self.__millas_acum:
            print("Error")
        else:
            self.__millas_acum -= millas_canje
        return self.cantidadTotalMillas()

    def __gt__(self, otro):
        return self.__millas_acum > otro.cantidadTotalMillas()
    
    def __add__ (self, valor):
        self.__millas_acum = self.__millas_acum + valor
        return self
    
    def __radd__(self, valor):
        self.__millas_acum = valor + self.__millas_acum
        return self
    
    def __sub__ (self, valor):
        self.__millas_acum = self.__millas_acum - valor
        return self
    
    def __rsub__ (self, valor):
        self.__millas_acum = -(valor - self.__millas_acum)
        return self
    
    def __eq__ (self, valor):
        return self.__millas_acum == valor 
    
