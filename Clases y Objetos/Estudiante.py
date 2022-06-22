class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self._nombre = nombre
        self._carrera = carrera
        self._semestre = semestre

    def __str__(self):
        return f'Estudiante [nombre: {self._nombre}, carrera:{self._carrera}, semestre:{self._semestre}]'

    def obtenernombre(self):  # getNombre
        return self._nombre,

    def obtenerCarrera(self):
        return self._carrera

    def obtenerSemestre(self):
        return self._semestre

    def modificarNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def modificarCarrera(self, nuevaCarrera):
        self._carrera = nuevaCarrera

    def modifcarSemestre(self, nuevoSemetre):
        self._semestre = nuevoSemetre

    def matricular_estudiante(self, nota_semestre_anterior):
        if nota_semestre_anterior >= 7:
            return True
        else:
            return False

objE1 = Estudiante('Luis', 'LGIG', '3')
print(objE1)
objE1.modifcarSemestre(4)
print(f'Nuevo semestre es: {objE1.obtenerSemestre()}')
print(objE1)
print(f"El estudiante: {objE1.obtenernombre()}, se matriculo?: {objE1.matricular_estudiante(8)}")