from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho:int=None, alto:int=None):
        super(Rectangulo, self).__init__(alto=alto, ancho=ancho)

    def __str__(self):
        return f'Rectangulo [ancho: {self.ancho}, alto: {self.alto}]'

    # def calcular_area(self):
    #     return self.ancho * self.alto

if __name__=='__main__':
    r1 = Rectangulo(ancho=5,alto=9)
    print(r1)
    print(f'El area del rectangulo es: {r1.calcular_area()}')