# Versión 4

# En este hay restricciones de dominio en los depertamentos y métodos de str para imprimir por pantalla los objetos y verificar que lo que estamos haciando funciona.

class Persona:
    def __init__(self, nombre, DNI, direccion, sexo):
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo

    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo}"

class Asignatura:
    def __init__(self, nombre, creditos, curso):
        self.nombre = nombre
        self.creditos = creditos # Atributos adicionales que no pide pero son coherentes en el contexto.
        self.curso = curso
        
    def __str__(self):
        return f"Asignatura: {self.nombre} \nCréditos: {self.creditos} \nCurso: {self.curso}"


class Profesor(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        if departamento not in ["DIIC", "DITEC", "DIS"]: # Aquí metemos la restricción con los departamentos que nos da el enunciado.
            raise ValueError("El Departamento debe ser uno de los siguientes: DIIC, DITEC o DIS") # Control de errrores.
        else:
            self.departamento = departamento
        
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas_impartidas = []
    
    def impartir_asignatura(self, asignatura):
        self.asignaturas_impartidas.append(asignatura)

    def dejar_impartir_asignatura(self, asignatura):
        self.asignaturas_impartidas.remove(asignatura)

    def cambiar_departamento(self, nuevo_departamento):
        if nuevo_departamento in ["DIIC", "DITEC", "DIS"]:
            self.departamento = nuevo_departamento
        else:
            raise ValueError("El Departamento debe ser uno de los siguientes: DIIC, DITEC o DIS") # COontrol de eerrores y dominio como antes.

    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_impartidas])
        return f"Profesor: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nAsignaturas impartidas: {asignaturas}"


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        super().__init__(nombre, DNI, direccion, sexo, departamento)
    
    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_impartidas])
        return f"Profesor Asociado: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nAsignaturas impartidas: {asignaturas}"


class ProfesorTitular(Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, area_investigador):
        super().__init__(nombre, DNI, direccion, sexo, departamento)
        self.area_investigador = area_investigador

    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_impartidas])
        return f"Profesor Titular: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nÁrea de Investigación: {self.area_investigador} \nAsignaturas impartidas: {asignaturas}"


class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo):
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas_matriculadas = []
    
    def agregar_asignatura_matriculada(self, asignatura):
        self.asignaturas_matriculadas.append(asignatura)

    def eliminar_asignatura_matriculada(self, asignatura):
        self.asignaturas_matriculadas.remove(asignatura)

    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_matriculadas])
        return f"Estudiante: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nAsignaturas Matriculadas: {asignaturas}"

# Ejemplo de uso
prof_asociado = ProfesorAsociado("Juan", "12345", "Calle 123", "M", "DIIC")
matematicas = Asignatura("Matemáticas", 5, "1º")
prof_asociado.impartir_asignatura(matematicas)
print(prof_asociado.asignaturas_impartidas)

prof_titular = ProfesorTitular("María", "54321", "Calle 456", "V", "DITEC", "area aleatoria")
fisica = Asignatura("Física", 4, "2º")
prof_titular.impartir_asignatura(fisica)

estudiante = Estudiante("Ana", "98765", "Calle 012", "V")
estudiante.agregar_asignatura_matriculada(matematicas)
estudiante.agregar_asignatura_matriculada(fisica)
print(estudiante.asignaturas_matriculadas)



# Código de prueba:

# Crear instancias de profesores titulares
prof_titular_1 = ProfesorTitular("María", "54321", "Calle 456", "V", "DITEC", "Área de investigación 1")
prof_titular_2 = ProfesorTitular("Juan", "65432", "Calle 789", "M", "DIIC", "Área de investigación 2")
prof_titular_3 = ProfesorTitular("Luisa", "76543", "Calle 012", "V", "DITEC", "Área de investigación 3")

# Crear instancias de profesores asociados
prof_asociado_1 = ProfesorAsociado("Carlos", "87654", "Calle 123", "M", "DIIC")
prof_asociado_2 = ProfesorAsociado("Ana", "98765", "Calle 456", "V", "DITEC")
prof_asociado_3 = ProfesorAsociado("Pedro", "09876", "Calle 789", "M", "DIIC")

# Crear instancias de estudiantes
estudiante_1 = Estudiante("Laura", "12345", "Calle 123", "V")
estudiante_2 = Estudiante("Lucas", "23456", "Calle 456", "M")
estudiante_3 = Estudiante("Marta", "34567", "Calle 789", "V")

# Crear instancias de asignaturas
asignatura_1 = Asignatura("Matemáticas", 5, "1º")
asignatura_2 = Asignatura("Física", 4, "2º")
asignatura_3 = Asignatura("Química", 3, "1º")
asignatura_4 = Asignatura("Biología", 3, "2º")
asignatura_5 = Asignatura("Historia", 2, "3º")
asignatura_6 = Asignatura("Literatura", 2, "3º")
asignatura_7 = Asignatura("Arte", 2, "4º")
asignatura_8 = Asignatura("Música", 2, "4º")
asignatura_9 = Asignatura("Programación", 4, "2º")
asignatura_10 = Asignatura("Inglés", 3, "1º")

# Asignar asignaturas a cada profesor titular
prof_titular_1.impartir_asignatura(asignatura_1)
prof_titular_1.impartir_asignatura(asignatura_2)
prof_titular_1.impartir_asignatura(asignatura_3)

prof_titular_2.impartir_asignatura(asignatura_4)
prof_titular_2.impartir_asignatura(asignatura_5)
prof_titular_2.impartir_asignatura(asignatura_6)

prof_titular_3.impartir_asignatura(asignatura_7)
prof_titular_3.impartir_asignatura(asignatura_8)
prof_titular_3.impartir_asignatura(asignatura_9)

# Asignar asignaturas a cada profesor asociado
prof_asociado_1.impartir_asignatura(asignatura_1)
prof_asociado_1.impartir_asignatura(asignatura_3)
prof_asociado_1.impartir_asignatura(asignatura_5)

prof_asociado_2.impartir_asignatura(asignatura_2)
prof_asociado_2.impartir_asignatura(asignatura_4)
prof_asociado_2.impartir_asignatura(asignatura_6)

prof_asociado_3.impartir_asignatura(asignatura_3)
prof_asociado_3.impartir_asignatura(asignatura_5)
prof_asociado_3.impartir_asignatura(asignatura_7)

# Matricular asignaturas para cada estudiante
estudiante_1.agregar_asignatura_matriculada(asignatura_1)
estudiante_1.agregar_asignatura_matriculada(asignatura_4)
estudiante_1.agregar_asignatura_matriculada(asignatura_7)

estudiante_2.agregar_asignatura_matriculada(asignatura_2)
estudiante_2.agregar_asignatura_matriculada(asignatura_5)
estudiante_2.agregar_asignatura_matriculada(asignatura_8)

estudiante_3.agregar_asignatura_matriculada(asignatura_3)
estudiante_3.agregar_asignatura_matriculada(asignatura_6)
estudiante_3.agregar_asignatura_matriculada(asignatura_9)


# Imprimir detalles de todos los profesores
print("Profesores Titulares:")
print(str(prof_titular_1))
print(str(prof_titular_2))
print(str(prof_titular_3))

print("\nProfesores Asociados:")
print(str(prof_asociado_1))
print(str(prof_asociado_2))
print(str(prof_asociado_3))

# Imprimir detalles de todos los estudiantes
print("\nEstudiantes:")
print(str(estudiante_1))
print(str(estudiante_2))
print(str(estudiante_3))
