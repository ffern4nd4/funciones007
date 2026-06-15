#funciones
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

#codigo principal
#declaro lista de mascotas
listas_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()