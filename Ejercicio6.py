class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, num_viajero, nombre, apellido, dni, millas_acum):
        self.__num_viajero = num_viajero
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__millas_acum = int(millas_acum)
    def cantidadTotalMillas (self):
        return self.__millas_acum
    def __add__ (self, num):
        self.__millas_acum = self.__millas_acum + num
        return self
    def __sub__ (self, millasXcanjear):
        if millasXcanjear <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - millasXcanjear
        else:
            print ('Error en la operacion: Cantidad de millas insuficiente.')
        return self
    def buscar (self, num):
        marca = False
        if num == self.__num_viajero:
            marca = True
        return marca
    def __gt__ (self, otroViajero):
        bul = False
        if self.__millas_acum > otroViajero.__millas_acum:
            bul = True
        return bul
    def getNombre (self):
        return self.__nombre+' '+self.__apellido
    def mostrar (self):
        print (self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)