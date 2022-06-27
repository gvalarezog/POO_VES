

class Vehiculo:
    def __init__(self, matriculado:bool, placa:str=None, marca:str=None, modelo:str=None, anio:int=None):
        self._marca = marca
        self._modelo = modelo
        self._anio =  anio
        self._matriculado = matriculado
        self._placa = placa

    def __str__(self):
        return f'Vehiculo [marca: {self._marca}, modelo: {self._modelo}, año: {self._anio}, ' \
               f'Esta Matriculado?: {self._matriculado}, placa: {self._placa}]'

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def matriculado(self):
        return self._matriculado

    @matriculado.setter
    def matriculado(self, matriculado):
        self._matriculado = matriculado

    @property
    def placa(self):
        return self._placa

    # @placa.setter
    # def placa(self, placa):
    #     self._placa = placa

if __name__=='__main__':
    # carro1 = Vehiculo(matriculado=True, modelo='Sail', marca='Chevrolet', anio=2022, placa='GYZ-01234')
    # print(carro1)
    # # print(carro1.marca)
    # # print(carro1._marca)
    # # carro1._marca = 'Ford'
    # # carro1.marca = 'Suzuki'
    # # print(carro1.marca)
    # # print(carro1.modelo)
    # # print(carro1.matriculado)
    # # print(carro1.anio)
    # carro1.matriculado = False
    #
    # # print(f'El vehculo está matriculado? {carro1.matriculado}')
    # # carro1.placa = 'GYZ-9876'
    # print(carro1)
    #
    #
    # carro2 = Vehiculo('POI-2558')
    # print(carro2)
    # carro2.marca = 'Ford'
    # carro2.modelo = 'F150'
    # carro2.anio = 2020
    # carro2.matriculado = True
    # carro2._placa = 'TGV-9632'
    # print(carro2)

    # print(carro1 == carro2)

    carro3 = Vehiculo(placa='GCR-8974', modelo='Seltos', marca='KIA', matriculado=True, anio='Dos mil veinte')
    print(carro3)

    carro4 = Vehiculo(True)
    print(carro4)
