class Celula:
    def __init__(self):
        self.__proxima = None
        self.__elemento = None
 
    @property
    def proxima(self):
        return self.__proxima
 
    @proxima.setter
    def proxima(self, proxima):
        self.__proxima = proxima
 
    @property
    def elemento(self):
        return self.__elemento
