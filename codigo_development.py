# Versión 3

# En esta versión del código se cambia el planteamiento del enunciado y interpretamos de forma distinta el concepto de miembro de departamento
# y de investigador, asumiendo que todos los investigadores son profesores titulares y estas dos clases se solapan completamente, y que todos los miembros de departamento son profesores.
class Persona:
    def __init__(self, nombre, DNI, direccion, sexo):
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo

class Profesor(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas_impartidas = []
        self.departamento = departamento
    
    def impartir_asignatura(self, asignatura):
        self.asignaturas_impartidas.append(asignatura)

    def dejar_impartir_asignatura(self, asignatura):
        self.asignaturas_impartidas.remove(asignatura)

    def cambiar_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento

class ProfesorAsociado(Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        Persona.__init__(self, nombre, DNI, direccion, sexo)
        Profesor.__init__(self, nombre, DNI, direccion, sexo, departamento)

class ProfesorTitular(Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, area_investigador):
        Persona.__init__(self, nombre, DNI, direccion, sexo)
        Profesor.__init__(self, nombre, DNI, direccion, sexo, departamento)
        self.area_investigador = area_investigador

class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo):
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas_matriculadas = []
    
    def agregar_asignatura_matriculada(self, asignatura):
        self.asignaturas_matriculadas.append(asignatura)

    def eliminar_asignatura_matriculada(self, asignatura):
        self.asignaturas_matriculadas.remove(asignatura)

# Ejemplo de uso
prof_asociado = ProfesorAsociado(85, "12345", "Calle 123", "M", "DIIC")
prof_asociado.impartir_asignatura("Matemáticas")
print(prof_asociado.asignaturas_impartidas)

prof_titular = ProfesorTitular("María", "54321", "Calle 456", "V", "DITEC", "area aleatoria")
prof_titular.impartir_asignatura("Física")


estudiante = Estudiante("Ana", "98765", "Calle 012", "V")
