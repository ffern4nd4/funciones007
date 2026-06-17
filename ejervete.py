#funciones
#validaciones

def validar_nombre(name):
    #una funcion de python que elimina los espacios al inicio o al final de un string y si queda vacia devuelve un False
    return name.strip() != " " #retorna True si es valido - False si es invalido
def validar_especie(race):
    #verificar que es perro, gato o ave solamente (sin diferenciar mayusuclas o minusculas)
    especies_validas = ["gatos", "perro", "ave"]
    return race.strip().lower() in especies_validas
def validar_edad(age):
    #validar que sean numeros y mayor a 0
    #isdigit() --> revisa que el string contenga solo digitos (no negativo, no digital)
    return age.isdigit() and int(age) > 0

def mostrar_menu():
    print(" ¨¨¨¨¨¨¨¨ MENU ¨¨¨¨¨¨¨¨")
    print("|| 1.-Agregar mascota ||")
    print("|| 2.-Buscar mascota  ||")
    print("|| 3.-ELiminar mascota ||")
    print("|| 4.-Marcar mascota como vacunada ||")
    print("|| 5.-Mostrar mascota ||")
    print("|| 6.-Salir           ||")
    print(" ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Ingrese un numero del 1 al 6")
            else:
                break
        except ValueError:
            print("Ingrese un numero")
    return opcion

def agregar_mascota(lista):
    nombre = input("Ingrese el nombre de la mascota: ")
    #llamar la funcion que valida el nombre para mostrar el mensaje
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar vacio")
        return 

    especie = input("Ingrese la especie de la mascota (perro, grato, ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La especie solo puede ser gato, perro o ave")
        return
    
    edad = input("Ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
    if not correcto:
        print("La edad debe ser un numero entero mayor a cero")
        return
    #aqui agrego al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agrego a la lista
    lista.append(mascota)

#codigo principal
#declaro lista de mascotas
listas_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(listas_mascotas)
    elif op == 2:
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print()