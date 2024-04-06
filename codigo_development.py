# Versión 8

# Clases para crear objetos génericos que valen para cualquier universidad.
# Operaciones y restricciones básicas que aplican a todos los casos.

class Persona:
    def __init__(self, nombre, apellidos, DNI, direccion, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo

    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo}"


class Asignatura:
    def __init__(self, nombre, codigo, creditos, curso):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.curso = curso
        
    def __str__(self):
        return f"Asignatura: {self.nombre} \nCódigo: {self.codigo} \nCréditos: {self.creditos} \nCurso: {self.curso}"


class Profesor(Persona):
    def __init__(self, nombre, apellidos, DNI, direccion, sexo, departamento):
        super().__init__(nombre, apellidos, DNI, direccion, sexo)
        self.asignaturas_impartidas = set()
        self.departamento = departamento
    
    def impartir_asignatura(self, asignatura):
        self.asignaturas_impartidas.add(asignatura)

    def dejar_impartir_asignatura(self, asignatura):
        if asignatura in self.asignaturas_impartidas:
            self.asignaturas_impartidas.remove(asignatura)
        else:
            raise ValueError("La asignatura no se encuentra entre las impartidas.")

    def cambiar_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento

    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_impartidas])
        return f"Profesor: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nAsignaturas impartidas: {asignaturas}"


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, apellidos, DNI, direccion, sexo, departamento):
        super().__init__(nombre, apellidos, DNI, direccion, sexo, departamento)
    
    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_impartidas])
        return f"Profesor Asociado: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nAsignaturas impartidas: {asignaturas}"


class ProfesorTitular(Profesor):
    def __init__(self, nombre, apellidos, DNI, direccion, sexo, departamento, area_investigador):
        super().__init__(nombre, apellidos, DNI, direccion, sexo, departamento)
        self.area_investigador = area_investigador

    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_impartidas])
        return f"Profesor Titular: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nÁrea de Investigación: {self.area_investigador} \nAsignaturas impartidas: {asignaturas}"


class Estudiante(Persona):
    def __init__(self, nombre, apellidos, DNI, direccion, sexo):
        super().__init__(nombre, apellidos, DNI, direccion, sexo)
        self.asignaturas_matriculadas = set()
    
    def agregar_asignatura_matriculada(self, asignatura):
        self.asignaturas_matriculadas.add(asignatura)

    def eliminar_asignatura_matriculada(self, asignatura):
        if asignatura in self.asignaturas_matriculadas:
            self.asignaturas_matriculadas.remove(asignatura)
        else:
            raise ValueError("La asignatura no se encuentra matriculada.")

    def __str__(self):
        asignaturas = ', '.join([asig.nombre for asig in self.asignaturas_matriculadas])
        return f"Estudiante: {self.nombre} \nDNI: {self.DNI} \nDirección: {self.direccion} \nSexo: {self.sexo} \nAsignaturas Matriculadas: {asignaturas}"


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = []
        self.profesores = []
        self.estudiantes = []
        self.departamentos = ['DIIC', 'DITEC', 'DIS'] # Añadimos los departamentos que hay en la universidad.

    def __str__(self): # Como esto es muy largo lo ponemos de una en una.
        return f"Universidad {self.nombre}\n" \
               f"Número de profesores: {len(self.profesores)}\n" \
               f"{self.profesores}\n" \
               f"Número de estudiantes: {len(self.estudiantes)}\n" \
               f"{self.estudiantes}\n" \
               f"Número de asignaturas: {len(self.asignaturas)}\n" \
               f"{self.asignaturas}\n" \
               f"Departamentos: {self.departamentos}\n"
               
    def crear_profesor(self, nombre, apellidos, DNI, direccion, sexo, departamento, area_investigador=None):
        # Verificar si el profesor ya existe con el mismo DNI.
        if any(profesor.DNI == DNI for profesor in self.profesores):
            raise ValueError ("Ya existe un profesor con este DNI.")
        else:
            if area_investigador:
                profesor = ProfesorTitular(nombre, apellidos, DNI, direccion, sexo, departamento, area_investigador) 
            else:
                profesor = ProfesorAsociado(nombre, apellidos, DNI, direccion, sexo, departamento)
            self.profesores.append(profesor)
            return profesor

    def crear_estudiante(self, nombre, apellidos, DNI, direccion, sexo):
        # Verificar si el estudiante ya existe con el mismo DNI.
        if any(estudiante.DNI == DNI for estudiante in self.estudiantes):
            raise ValueError ("Ya existe un estudiante con este DNI.")
        else:
            estudiante = Estudiante(nombre, apellidos, DNI, direccion, sexo)
            self.estudiantes.append(estudiante)
            return estudiante

    def crear_asignatura(self, nombre, codigo, creditos, curso):
        # Verificar si la asignatura ya existe con el mismo código o nombre.
        if any(asignatura.codigo == codigo for asignatura in self.asignaturas) or any(asignatura.nombre == nombre for asignatura in self.asignaturas):
            raise ValueError ("Ya existe una asignatura con este código o nombre.")
        else:
            asignatura = Asignatura(nombre, codigo, creditos, curso)
            self.asignaturas.append(asignatura)
            return asignatura

    def eliminar_profesor(self, profesor):
        if profesor in self.profesores:
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

    def mostrar_profesores(self):
        print("Profesores:")
        for profesor in self.profesores:
            print(profesor)

    def mostrar_profesores_asociados(self):
        print("Profesores Asociados:")
        for profesor in self.profesores:
            if isinstance(profesor, ProfesorAsociado):
                print(profesor)

    def mostrar_profesores_titulares(self):
        print("Profesores Titulares:")
        for profesor in self.profesores:
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

# **kwargs como parámetro en una función, significa que la función aceptará cualquier cantidad de argumentos keyworded 
# y los recibirá en forma de un diccionario, donde las claves son los nombres de los argumentos y 
# los valores son los valores pasados a esos argumentos.
    def buscar_asignatura(self, **kwargs):
        """
        Busca una asignatura en la universidad según los atributos dados.
        Los atributos permitidos son 'nombre', 'codigo', 'creditos' y 'curso'.
        """
        # Inicializamos una lista vacía para almacenar los resultados de la búsqueda.
        resultados = []
        # Iteramos sobre la lista de asignaturas para buscar coincidencias.
        for asignatura in self.asignaturas:
            coincide = True  # Variable para controlar si la asignatura coincide con los criterios de búsqueda.
            # Iteramos sobre los pares clave-valor en kwargs para verificar si la asignatura coincide con los criterios.
            for key, value in kwargs.items():
                # Comparamos el valor del atributo de la asignatura con el valor especificado en kwargs.
                if getattr(asignatura, key, None) != value:
                    coincide = False  # Si hay una diferencia, la asignatura no coincide.
                    break  # Salimos del bucle interno si ya no coincide con un criterio.
            # Si la asignatura coincide con todos los criterios de búsqueda, la añadimos a los resultados.
            if coincide:
                resultados.append(asignatura)
        # Si se encontraron asignaturas que coinciden, las mostramos por pantalla.
        if resultados:
            print("Asignaturas encontradas:")
            for asignatura in resultados:
                print(asignatura)
        else:
            raise ValueError("No se encontraron asignaturas con los atributos dados.")
        
    def buscar_estudiante(self, **kwargs):
        """
        Busca un estudiante en la universidad según los atributos dados.
        Los atributos permitidos son 'nombre', 'apellidos', 'DNI', 'direccion' y 'sexo'.
        """
        resultados = []
        for estudiante in self.estudiantes:
            coincide = True
            for key, value in kwargs.items():
                if getattr(estudiante, key, None) != value:
                    coincide = False
                    break
            if coincide:
                resultados.append(estudiante)
        if resultados:
            print("Estudiantes encontrados:")
            for estudiante in resultados:
                print(estudiante)
        else:
            raise ValueError ("No se encontraron estudiantes con los atributos dados.")

    def buscar_profesor(self, **kwargs):
        """
        Busca un profesor en la universidad según los atributos dados.
        Los atributos permitidos son 'nombre', 'apellidos', 'DNI', 'direccion', 'sexo', 'departamento' y 'area_investigador'.
        """
        resultados = []
        for profesor in self.profesores:
            coincide = True
            for key, value in kwargs.items():
                if key == 'area_investigador':
                    # Verificar si el profesor tiene área de investigación y si coincide con el valor dado.
                    if not hasattr(profesor, 'area_investigador') or getattr(profesor, 'area_investigador') != value:
                        coincide = False
                        break
                elif getattr(profesor, key, None) != value:
                    coincide = False
                    break
            if coincide:
                resultados.append(profesor)
        if resultados:
            print("Profesores encontrados:")
            for profesor in resultados:
                print(profesor)
        else:
           raise ValueError ("No se encontraron profesores con los atributos dados.")
    
# La restriccion de que solo se pueda meter una asignatura pra impartir o matricular si existe en la universidad
# la añadimos aqui y no en la clase de profesir y alumno porque en ellas no tenemos disposicion de la lista total de asignaturas
# de la que si disponemos en la clase universidad.
    def matricular_asignatura(self, alumno, asignatura):
        """
        Matricula a un alumno en una asignatura si la asignatura existe en la lista de asignaturas de la universidad.

        Parámetros:
            - alumno (Estudiante): Objeto Estudiante a matricular.
            - asignatura (Asignatura): Objeto Asignatura en la cual matricular al alumno.
        """
        if asignatura in self.asignaturas:
            alumno.agregar_asignatura_matriculada(asignatura)
        else:
            raise ValueError (f"La asignatura {asignatura.nombre} no existe en la universidad.")

    def desmatricular_asignatura(self, alumno, asignatura):
        """
        Desmatricula a un alumno de una asignatura.

        Parámetros:
            - alumno (Estudiante): Objeto Estudiante a desmatricular.
            - asignatura (Asignatura): Objeto Asignatura de la cual desmatricular al alumno.
        """
        alumno.eliminar_asignatura_matriculada(asignatura)

    def impartir_asignatura(self, profesor, asignatura):
        """
        Asigna a un profesor para que imparta una asignatura si la asignatura existe en la lista de asignaturas de la universidad.

        Parámetros:
            - profesor (Profesor): Objeto Profesor que va a impartir la asignatura.
            - asignatura (Asignatura): Objeto Asignatura que va a ser impartida por el profesor.
        """
        if asignatura in self.asignaturas:
            profesor.impartir_asignatura(asignatura)
        else:
            raise ValueError (f"La asignatura {asignatura.nombre} no existe en la universidad.")

    def dejar_impartir_asignatura(self, profesor, asignatura):
        """
        Deja de asignar a un profesor para que imparta una asignatura.

        Parámetros:
            - profesor (Profesor): Objeto Profesor que dejará de impartir la asignatura.
            - asignatura (Asignatura): Objeto Asignatura que dejará de ser impartida por el profesor.
        """
        profesor.dejar_impartir_asignatura(asignatura)

    def cambiar_departamento(self, profesor, nuevo_dep):
        """
        Permite a un profesor cambiarse de departamento.

        Parámetros:
            - profesor (Profesor): El objeto profesor que quiere cambiarse de departamento.
            - nuevo_dep (str): El nombre del nuevo departamento al cual se va a integrar el profesor.
        """
        if nuevo_dep in self.departamentos:
            profesor.cambiar_departamento(nuevo_dep)
        else:
            raise ValueError (f"El Departamento {nuevo_dep} no existe en esta Universidad.")

    def listar_imparticion(self, asignatura=None):
        """
        Devuelve una lista de profesores que imparten la asignatura proporcionada.
        Si no se proporciona ninguna asignatura, devuelve una lista de todas las asignaturas impartidas por cada profesor.

        Parámetros:
            - asignatura (Asignatura, opcional): Objeto Asignatura para filtrar los profesores que la imparten.
        """
        if asignatura: #y si la asignatura no existe?
            if asignatura in self.asignaturas:
                print(f"Profesores que imparten {asignatura.nombre}:")
                for profesor in self.profesores:
                    if asignatura in profesor.asignaturas_impartidas:
                        print(profesor)
            else:
                raise ValueError (f"La asignatura {asignatura} no existe.")
        else:
            print("Listado de todas las asignaturas impartidas por cada profesor:")
            for profesor in self.profesores:
                print(f"Profesor: {profesor.nombre}")
                for asignatura in profesor.asignaturas_impartidas:
                    print(f"\t{asignatura}")

    def listar_matriculados(self, asignatura):
        """
        Muestra la lista de estudiantes matriculados en una asignatura.

        Parámetros:
            - asignatura (Asignatura): La asignatura para la cual se desea listar los estudiantes matriculados.
        """
        #y si la asignatura no existe?
        if asignatura in self.asignaturas:
            print(f"Estudiantes matriculados en {asignatura.nombre}:")
            for estudiante in self.estudiantes:
                if asignatura in estudiante.asignaturas_matriculadas:
                    print(estudiante)
        else:
                raise ValueError (f"La asignatura {asignatura} no existe.")        


# No hace falta una clase de departameto porqeu solamente existen 3 y no interesa crear ni eliminar ninguno de ellos, así mismo todos los profesores deben pertenecer a algún deparatamento
# el cual se declara cuando se define el objeto profesor, y la unica forma en la que un profesor puede salir de un departamento es, 1) cambiando de deparatmento (debe pertenercer a 1)
# 2) dejando de trabajar para la univerdidad, en cuyo caso se elimina direcatemte el objeto profesor
# no necesitamos ningun otro metodo para departamento porqeu seria redundante.
    def listar_miembros_departamento(self, departamento):
        """
        Lista los miembros (profesores) de un departamento dado.

        Parámetros:
            - departamento (str): El nombre del departamento del cual se desean listar los miembros.
        """
        if departamento in self.departamentos: # Verificamos que el departamento insertado existe en la lista de la uni.
            print(f"Miembros del departamento {departamento}:")
            for profesor in self.profesores:
                if profesor.departamento == departamento:
                    print(f"{profesor.nombre} {profesor.apellidos}")
        else:
            raise ValueError (f"El departamento {departamento} no existe.")


# Ejemplo de uso
universidad = Universidad('UPCT')

# Crear profesor titular
prof_titular = universidad.crear_profesor("María", "García", "54321", "Calle 456", "V", "DITEC", "Área de investigación 1")

# Crear estudiante
estudiante = universidad.crear_estudiante("Laura", "Pérez", "12345", "Calle 123", "V")

# Crear asignatura
asignatura = universidad.crear_asignatura("Matemáticas", 82345, 5, "1º")
asignatura = universidad.crear_asignatura("Química", 65415, 5, "1º")


# Mostrar listas
universidad.mostrar_profesores()
universidad.mostrar_estudiantes()
universidad.mostrar_asignaturas()


# Eliminar profesor
universidad.eliminar_profesor(prof_titular)

# Eliminar estudiante
universidad.eliminar_estudiante(estudiante)


# Mostrar listas
universidad.mostrar_profesores()
universidad.mostrar_estudiantes()
universidad.mostrar_asignaturas()


universidad.buscar_asignatura(nombre="Matemáticas")
universidad.buscar_asignatura(codigo=82345)
universidad.buscar_asignatura(creditos=5)


# Creamos algunos profesores para agregarlos a la lista de profesores de la universidad
profesor1 = universidad.crear_profesor("Juan", "Perez", "12345678A", "Calle 123", "M", "DIIC", "Área de investigación 1")
profesor2 = universidad.crear_profesor("María", "García", "87654321B", "Calle 456", "F", "DITEC", "Área de investigación 2")
profesor3 = universidad.crear_profesor("Ana", "López", "98765432C", "Calle 789", "F", "DIIC")

# Buscamos profesores que coincidan con ciertos atributos
universidad.buscar_profesor(nombre="Juan", departamento="DIIC")
universidad.buscar_profesor(sexo='F')

universidad.listar_miembros_departamento("DIIC")