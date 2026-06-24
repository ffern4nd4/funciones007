def mostrar_menu():
    print("******* MENU *******")
    print("1.- Agregar reserva")
    print("2.- Buscar reserva")
    print("3.- Eliminar reserva")
    print("4.- Confirmar reserva")
    print("5.- Mostrar reserva")
    print("6.- Salir")
    print("********************")

def ingresar_opcion():
    while True:
        try: 
            op = int(input("Seleccione una opcion: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except ValueError:
            print("Debe ingresar un numero del 1 al 6")

def agregar_reserva(lista_r):
    nombre_completo = input("Ingrese el nombre completo del huesped: ")
    correcto = validar_huesped(nombre_completo)
    if not correcto:
        print("El nombre no puede estar vacio")
        return
    numero_habitacion = input("Ingrese  el numero de habitacion a reservar: ")
    correcto = validar_habitacion(numero_habitacion)
    if not correcto:
        print("La habitacion debe ser un numero entero del 1 al 200")
        return

    cant_noches = input("Ingrese la cantidad de noches a hospedarse: ")
    correcto = validar_noches(cant_noches)
    if not correcto:
        print("La cantidad de noches debe ser mayor a 0")
        return
    
    reserva = {
        "huesped" : nombre_completo.strip().upper(),
        "habitacion" : int(numero_habitacion),
        "noches" : int(cant_noches),
        "confirmada" : False
    }
    lista_r.append(reserva)
    print("Reserva agregada correctamente")

def buscar_reserva(lista_r, huesped):
    for x in range(len(lista_r)):
        if huesped == lista_r[x]["huesped"]:
            return x
        
    return -1 

def confirmar_reservas(lista_r):
    for i in lista_r:
        if i["noches"] >= 2:
            i["confirmada"] = True
        else:
            i["confirmada"] = False

def mostrar_reservas(lista_r):
    print(" ======== Lista de Reservas ===========")
    for i in lista_r:
        print(f"Huesped: {i["huesped"]}")
        print(f"Habitacion: {i["habitacion"]}")
        print(f"Noches: {i["noches"]}")
    if i ["confirmada"]:
        print("estado: CONFIRMADA")
    else:
        print("estado: PENDIENTE")

def validar_huesped(nombre):
    return nombre.strip() != ""
def validar_habitacion(hab):
     if hab.isdigit():
         validar = int(hab)
         return validar >= 1 and validar <= 200
     return False
     
def validar_noches(noches):
    if noches.isdigit():
        validar = int(noches)
        return validar > 0
    return False