# Versión 2

class Persona:
    def __init__(self, nombre, DNI, direccion, sexo):
        # Aquí intentamos meter unas restricciones de dominio. Si no se cumplen, lanzaremos una excepción.
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string.")
        if not isinstance(DNI, str):
            raise TypeError("El DNI debe ser un string.")
        if not isinstance(direccion, str):
            raise TypeError("La dirección debe ser un string.")
        
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo

    def get_sexo(self):
        return self._sexo

    def set_sexo(self, value):
        if value.upper() not in ['V', 'M']:
            raise ValueError("El sexo debe ser 'V' o 'M'.")
        self._sexo = value.upper()

    sexo = property(get_sexo, set_sexo)

    

class MiembroDepartamento:
    def __init__(self, departamento):
        self.departamento = departamento
    
    def cambiarDepartamento(self, nuevoDepartamento):
        self.departamento = nuevoDepartamento

class Profesor(Persona):
    def __init__(self, nombre, DNI, direccion, sexo):
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturasImpartidas = []

class ProfesorAsociado(MiembroDepartamento, Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        Persona.__init__(self, nombre, DNI, direccion, sexo)
        MiembroDepartamento.__init__(self, departamento)
        Profesor.__init__(self, nombre, DNI, direccion, sexo)
    
    def impartirAsignatura(self, asignatura):
        self.asignaturasImpartidas.append(asignatura)

class ProfesorTitular(MiembroDepartamento, Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        Persona.__init__(self, nombre, DNI, direccion, sexo)
        MiembroDepartamento.__init__(self, departamento)
        Profesor.__init__(self, nombre, DNI, direccion, sexo)
    
    def impartirAsignatura(self, asignatura):
        self.asignaturasImpartidas.append(asignatura)
    
    def asignarRolInvestigador(self):
        print("Asignando rol de investigador")

class Investigador(Persona, MiembroDepartamento):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, areaInvestigacion):
        Persona.__init__(self, nombre, DNI, direccion, sexo)
        MiembroDepartamento.__init__(self, departamento)
        self.areaInvestigacion = areaInvestigacion

class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo):
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturasMatriculadas = []

# Ejemplo de uso
prof_asociado = ProfesorAsociado("Juan", "12345", "Calle 123", "M", "DIIC")
prof_asociado.impartirAsignatura("Matemáticas")
print(prof_asociado.asignaturasImpartidas)

prof_titular = ProfesorTitular("María", "54321", "Calle 456", "V", "DITEC")
prof_titular.impartirAsignatura("Física")
prof_titular.asignarRolInvestigador()

investigador = Investigador("Carlos", "67890", "Calle 789", "M", "DIS", "Inteligencia Artificial")
print(investigador.areaInvestigacion)

estudiante = Estudiante("Ana", "98765", "Calle 012", "V")
