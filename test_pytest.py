import pytest
from codigo_final import Universidad, Persona, Asignatura, Profesor, ProfesorAsociado, ProfesorTitular


# Creamos una fixture para instanciar la universidad en cada prueba.
@pytest.fixture(scope="module")
def universidad():
    return Universidad("Universidad de Prueba")

def test_crear_asignatura(universidad):
    asignatura = universidad.crear_asignatura("Matemáticas", 1041, 6, 1)
    assert asignatura.nombre == "Matemáticas"
    assert asignatura.codigo == 1041
    assert asignatura.creditos == 6
    assert asignatura.curso == 1

def test_crear_profesor(universidad):
    profesor = universidad.crear_profesor("Alberto", "Pérez", "12345678A", "Calle Todos los Santos", "V", "DIIC")
    assert profesor.nombre == "Alberto"
    assert profesor.apellidos == "Pérez"
    assert profesor.DNI == "12345678A"
    assert profesor.direccion == "Calle Todos los Santos"
    assert profesor.sexo == "V"
    assert profesor.departamento == "DIIC"

def test_crear_estudiante(universidad):
    estudiante = universidad.crear_estudiante("Pedro", "Martínez", "54816852J", "Calle Ramón y Cajal", "V")
    assert estudiante.nombre == "Pedro"
    assert estudiante.apellidos == "Martínez"
    assert estudiante.DNI == "54816852J"
    assert estudiante.direccion == "Calle Ramón y Cajal"
    assert estudiante.sexo == "V"

def test_eliminar_asignatura(universidad):
    asignatura = universidad.crear_asignatura("Física", 1028, 6, 1)
    universidad.eliminar_asignatura(asignatura)
    assert asignatura not in universidad.asignaturas

def test_eliminar_profesor(universidad):
    profesor = universidad.crear_profesor("María", "López", "87654321B", "Calle La Marina", "M", "DITEC")
    universidad.eliminar_profesor(profesor)
    assert profesor not in universidad.profesores

def test_eliminar_estudiante(universidad):
    estudiante = universidad.crear_estudiante("Luis", "González", "98765432C", "Avenida Del Carmen", "V")
    universidad.eliminar_estudiante(estudiante)
    assert estudiante not in universidad.estudiantes

def test_mostrar_estudiantes(universidad, capsys):
    universidad.mostrar_estudiantes()
    captured = capsys.readouterr()
    assert "Estudiantes:\n" in captured.out

def test_mostrar_profesores(universidad, capsys):
    universidad.mostrar_profesores()
    captured = capsys.readouterr()
    assert "Profesores:\n" in captured.out

def test_mostrar_asignaturas(universidad, capsys):
    universidad.mostrar_asignaturas()
    captured = capsys.readouterr()
    assert "Asignaturas:\n" in captured.out

def test_mostrar_profesores_titulares(universidad, capsys):
    universidad.mostrar_profesores_titulares()
    captured = capsys.readouterr()
    assert "Profesores Titulares:\n" in captured.out

def test_mostrar_profesores_asociados(universidad, capsys):
    universidad.mostrar_profesores_asociados()
    captured = capsys.readouterr()
    assert "Profesores Asociados:\n" in captured.out

def test_buscar_asignatura(universidad, capsys):
    universidad.buscar_asignatura(nombre="Matemáticas")
    captured = capsys.readouterr()
    assert "Asignaturas encontradas:\nAsignatura: Matemáticas" in captured.out

def test_buscar_profesor(universidad, capsys):
    universidad.buscar_profesor(nombre="Alberto")
    captured = capsys.readouterr()
    assert "Profesores encontrados:\nProfesor Asociado: Alberto" in captured.out

def test_buscar_estudiante(universidad, capsys):
    universidad.buscar_estudiante(nombre="Pedro")
    captured = capsys.readouterr()
    assert "Estudiantes encontrados:\nEstudiante: Pedro" in captured.out

def test_matricular_asignatura(universidad):
    estudiante = universidad.crear_estudiante("Ana", "García", "87264915W", "Avenida Muralla", "M")
    asignatura = universidad.crear_asignatura("Matemáticas I", 1021, 6, 1)
    universidad.matricular_asignatura(estudiante, asignatura)
    assert asignatura in estudiante.asignaturas_matriculadas

def test_desmatricular_asignatura(universidad):
    estudiante = universidad.crear_estudiante("Antonia", "Remedios", "87254961L", "Avenida Napoleón", "M")
    asignatura = universidad.crear_asignatura("E.F.", 8715, 6, 3)
    universidad.matricular_asignatura(estudiante, asignatura)
    universidad.desmatricular_asignatura(estudiante, asignatura)
    assert asignatura not in estudiante.asignaturas_matriculadas

def test_impartir_asignatura(universidad):
    profesor = universidad.crear_profesor("Juan", "Pérez", "12345678B", "Calle Abastos", "V", "DIIC")
    asignatura = universidad.crear_asignatura("Matemáticas II", 1022, 6, 2)
    universidad.impartir_asignatura(profesor, asignatura)
    assert asignatura in profesor.asignaturas_impartidas

def test_dejar_impartir_asignatura(universidad):
    profesor = universidad.crear_profesor("Pilar", "Garrido", "97254615O", "Calle La Noria", "M", "DIIC")
    asignatura = universidad.crear_asignatura("Materiales", 8465, 6, 3)
    universidad.impartir_asignatura(profesor, asignatura)
    universidad.dejar_impartir_asignatura(profesor, asignatura)
    assert asignatura not in profesor.asignaturas_impartidas

def test_cambiar_departamento(universidad):
    profesor = universidad.crear_profesor("Ramona", "Torres", "89726451I", "Calle Calvario", "M", "DIIC")
    nuevo_departamento = "DITEC"
    universidad.cambiar_departamento(profesor, nuevo_departamento)
    assert profesor.departamento == nuevo_departamento

def test_listar_matriculados(universidad, capsys):
    estudiante = universidad.crear_estudiante("Elena", "González", "11111111A", "Avenida Carlos Manuel", "M")
    asignatura = universidad.crear_asignatura("Programación", 9746, 6, 2)
    universidad.matricular_asignatura(estudiante, asignatura)

    universidad.listar_matriculados(asignatura)
    captured = capsys.readouterr()
    assert "Estudiantes matriculados en Programación" in captured.out
    assert "Estudiante: Elena" in captured.out

def test_listar_miembros_departamento(universidad, capsys):
    profesor1 = universidad.crear_profesor("Carlos", "Martínez", "84912648P", "Calle Fleming", "V", "DIIC")
    profesor2 = universidad.crear_profesor("Laura", "Rodríguez", "87654321C", "Calle Neruda", "M", "DIS")

    universidad.listar_miembros_departamento("DIIC")
    captured = capsys.readouterr()
    assert "Miembros del departamento DIIC" in captured.out
    assert "Carlos Martínez" in captured.out

def test_listar_imparticion(universidad, capsys):
    asignatura = universidad.crear_asignatura("Programación Avanzada", 1031, 6, 3)
    profesor1 = universidad.crear_profesor("Pedro", "López", "98765432D", "Calle Velveto", "V", "DIIC")
    universidad.impartir_asignatura(profesor1, asignatura)

    universidad.listar_imparticion(asignatura)
    captured = capsys.readouterr()
    assert "Profesores que imparten Programación Avanzada" in captured.out
    assert "Profesor Asociado: Pedro" in captured.out

