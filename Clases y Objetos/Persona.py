
class Persona:
    #Atributos
    def __init__(self, nombre, genero, ocupacion, mail):
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._mail = mail

    #Metodos
    def __str__(self):
        return f'Persona: [nombre={self._nombre}, genero={self._genero}, ocupacion={self._ocupacion}, ' \
               f'mail={self._mail}]'

    def obtenerNombre(self):
        return self._nombre

    def obtenerGenero(self):
        return self._genero

    def modificarOcupacion(self, nuevaOcupacion):
        self._ocupacion = nuevaOcupacion
















objPersona1 = Persona('Guillemro', 'M', 'Docente', 'guillermo@mail.com')
objPersona2 = Persona('Maria', 'F', 'Estudiante', 'maria@mail.com')


print(type(objPersona1))
print(objPersona1.obtenerNombre())
print(objPersona1._genero)
print(objPersona1._ocupacion)
print(objPersona1)
#print(objPersona1.__str__())
print("**********************************")
# print(f'El nombre de la persona es: {objPersona2._nombre}')
# if objPersona2.obtenerGenero() == 'M':
#     print("El genero es masculino")
# else:
#     print("El genero es femenino")
# print(f'El correo es: {objPersona2._mail}')
# print(objPersona2)

objPersona1._mail = 'guillermo.v@mail.com'
objPersona1.modificarOcupacion('Estudiante')
print(objPersona1)

