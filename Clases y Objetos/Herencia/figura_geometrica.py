

class FiguraGeometrica:
    def __init__(self, ancho:int=0, alto:int=0):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return f'Figura Geometrica [ancho: {self._ancho}, alto: {self._alto}]'

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

if __name__=='__main__':
    f1 = FiguraGeometrica(4,5)
    print(f1)