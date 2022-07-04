from figura_geometrica import FiguraGeometrica

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio:int=None):
        super(Circunferencia, self).__init__(ancho=radio, alto=1)

    def __str__(self):
        return f'Circunferencia [radio: {self.ancho}]'

if __name__=='__main__':
    cir1 = Circunferencia(radio=6)
    print(cir1)
    print(f'El area de la circunferencia es: {cir1.calcular_area()}')