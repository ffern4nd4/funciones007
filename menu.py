import ejercicio_2_hotel as p

opcion = 0
lista_reservas = []

while opcion != 6:
    p.mostrar_menu()
    opcion = p.ingresar_opcion()
    if opcion == 1:
        #llamar a la funcion que ingresa reservas
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
            #solicite el nombre a buscar
            nombre = input("Ingrese el nombre del huesped a buscar: ")
            #llamamos a la funcion encargada de buscar
            pos = p.buscar_reserva(lista_reservas, nombre)
            #validamos que retorna la funcion de buscar
            if pos != -1:
                #se encontro el huespes asique muestro sus datos
                print("********** Reserva Encontrada ************")
                print(f"Nombre del huesped: {lista_reservas[pos]["huesped"]}")
                print(f"Numero de habitacion: {lista_reservas[pos]["habitacion"]}")
                print(f"Noches de hospedaje: {lista_reservas[pos]["noches"]}")
                estado = "CONFIRMADA" if lista_reservas[pos]["confirmada"] else "PENDIENTE"
                print(f"Estado: {estado}")
                print("*******************************************")
            else:
                print(f"El huesped '{nombre}' no ha sido encontrado")
    elif opcion == 3:
            #solicitamos el nombre a buscar
            nombre = input("Ingrese el nombre del huesped buscar")
            #llamamos a la funcion encargada de buscar
            pos = p.buscar_reserva(lista_reservas, nombre)
            #validamos que retorna la funcion de buscar
            if pos != -1:
                #encontramos el huesped asique procedemos a eliminar
                lista_reservas.pop(pos)
            else: 
                print(f"El huesped '{nombre}' no ha sido encontrado")
    elif opcion == 4:
         #llamamos a la funcion que confirma las reservas
         p.confirmar_reservas(lista_reservas)
    elif opcion == 5:
         #llamamos a la funcion que confirma las reservas
         p.confirmar_reservas(lista_reservas)
         p.mostrar_reservas(lista_reservas)
    elif opcion == 6:
         print("Gracias por usar el programa. Vuelva pronto!!!! madafaka")
    