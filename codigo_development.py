# Versión 6

# Para llevar las ideas claras hemos metido el código de la versión anterior en un fichero a parte y lo hemos importado todo para no tener una cantdiad
# masiva de código y poder trabajar solamente en la parte de la univerisidad como clase relacionada a las demás.


from version_5 import *

class Universidad: # La universidad va a almacenar todas las listas de cada tipo de objetos que nos interesa manipular y mostrar por pantalla.
    def __init__(self):
        self.asignaturas = []
        self.profesores = []
        self.estudiantes = []

    def crear_profesor(self, nombre, DNI, direccion, sexo, departamento, area_investigador=None):
        if area_investigador: # Dependiendo si tiene  o no un área de investigación se llama a una clase u otra.
            profesor = ProfesorTitular(nombre, DNI, direccion, sexo, departamento, area_investigador) # Utilizamos las clases de objetos creadas anteriormente en esta.
        else:
            profesor = ProfesorAsociado(nombre, DNI, direccion, sexo, departamento) # Cuando queramos hacer cualquier acción en la universidad siempre lo haremos a través de universidad y estas siemrpe se encargará de llamar a las clases correspondientes.
        self.profesores.append(profesor) # Y se añade a la lista correspondiente.
        return profesor

    # Hacemos lo mismo con el resto.
    def crear_estudiante(self, nombre, DNI, direccion, sexo):
        estudiante = Estudiante(nombre, DNI, direccion, sexo)
        self.estudiantes.append(estudiante)
        return estudiante

    def crear_asignatura(self, nombre, codigo, creditos, curso):
        asignatura = Asignatura(nombre, codigo, creditos, curso)
        self.asignaturas.append(asignatura)
        return asignatura

    def eliminar_profesor(self, profesor):
        if profesor in self.profesores: # Si existe lo eliminamos y si no lanzamos un error.
            self.profesores.remove(profesor)
        else:
            raise ValueError ("El profesor no existe en la universidad.")

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
        else:
            raise ValueError ("El estudiante no existe en la universidad.")

    def eliminar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
        else:
            raise ValueError ("La asignatura no existe en la universidad.")

    # Métodos para mostrar las listas.
    def mostrar_profesores(self):
        print("Profesores:")
        for profesor in self.profesores:
            print(profesor)

    def mostrar_profesores_asociados(self):
        print("Profesores Asociados:")
        for profesor in self.profesores:
            if isinstance(profesor, ProfesorAsociado): # Interesa filtrar por tipo de objeto dentro de profesor.
                print(profesor)

    def mostrar_profesores_titulares(self):
        print("Profesores Titulares:")
        for profesor in self.profesores: # Igual con titulares.
            if isinstance(profesor, ProfesorTitular):
                print(profesor)

    def mostrar_estudiantes(self):
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante)

    def mostrar_asignaturas(self):
        print("Asignaturas:")
        for asignatura in self.asignaturas:
            print(asignatura)


# Ejemplo de uso
universidad = Universidad()

# Crear profesor titular
prof_titular = universidad.crear_profesor("María", "54321", "Calle 456", "V", "DITEC", "Área de investigación 1")

# Crear estudiante
estudiante = universidad.crear_estudiante("Laura", "12345", "Calle 123", "V")

# Crear asignatura
asignatura = universidad.crear_asignatura("Matemáticas", 82345, 5, "1º")


# Mostrar listas
universidad.mostrar_profesores()
universidad.mostrar_estudiantes()
universidad.mostrar_asignaturas()


# Eliminar profesor
universidad.eliminar_profesor(prof_titular)

# Eliminar estudiante
universidad.eliminar_estudiante(estudiante)

# Eliminar asignatura
universidad.eliminar_asignatura(asignatura)


# Mostrar listas
universidad.mostrar_profesores()
universidad.mostrar_estudiantes()
universidad.mostrar_asignaturas()