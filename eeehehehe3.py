def mostrar_encabezado():
    print("[[------------------------]]")
    print("|| Sistema de admision escolar ||")
    print("[[------------------------]]")

def solicitar_datos():
    estudiantes = {}
    estudiantes["nombre"] = input("Indique el nombre del estudiante: ")
    estudiantes["rut"] = input("Indique el rut del estudiante: ")
    estudiantes["carrera"] = input("Indique la carrera del estudiante: ")
    while True:
        try:
            estudiantes["semestre"] = int(input("Indique el semestre que cursa el estudiante: "))
            if estudiantes["semestre"] <= 0 or estudiantes["semestre"] > 4:
                print("Ingrese un semestre valido")
            else:
                break
        except ValueError:
            print("Ingrese un numero")
    return estudiantes

def mostrar_datos(alumnos):
    print(f"Nombre del estudiante: {alumnos["nombre"]}")
    print(f"Rut del estudiante: {alumnos["rut"]}")
    print(f"Carrera del estudiante: {alumnos["carrera"]}")
    print(f"Semestre del estudiante: {alumnos["semestre"]}")

datos = solicitar_datos()
mostrar_encabezado()
mostrar_datos(datos)