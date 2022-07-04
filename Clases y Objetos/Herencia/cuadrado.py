from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado:int=0):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)


    def __str__(self):
        return f'Cuadrado [Lado: {self.ancho}]'

    # def calcular_area(self):
    #     return self.ancho * self.alto

if __name__=='__main__':
    cuadrado1 = Cuadrado(lado=5)
    print(cuadrado1)
    print(f'El area del cuadrado es: {cuadrado1.calcular_area()}')

