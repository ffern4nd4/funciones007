

def datos_producto(nombre, precio, stock):
    print("[=============================]")
    print(f"|| Nombre del producto: {nombre} ||")
    print(f"|| Stock del producto: {stock}   ||")
    print(f"|| Precio del producto: {precio} ||")
    print("[=============================]")

nombre1= input("Ingrese el nombre del producto: ")
while True:
    try:
        stock1= int(input("Ingrese el stock del producto    "))
        if stock1< 0:
            print("El stock debe ser mayor o igual a 0")
        else:
            break
    except ValueError:
        print("Ingrese un numero valido")


while True:
    try:
        precio1= int(input("Ingrese el precio del producto  "))
        if precio1<= 0:
            print("El precio debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("Ingrese un numero valido")
datos_producto(nombre1, precio1, stock1)