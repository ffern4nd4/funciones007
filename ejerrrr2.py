def conversion_puntaje(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return round(nota,1)

while True:
    try:
        p = float(input("Ingrese la nota del estudiante: "))
        if p < 0:
            print("Debe ingresar una nota valida")
        else: 
            break
    except ValueError:
        print("Debe ingresar un numero")

while True:
    try:
        pt = float(input("Ingrese la nota total de la evaluacion: "))
        if pt < 0 and pt < p:
            print("Debe ingresar una nota valida")
        else: 
            break
    except ValueError:
        print("Debe ingresar un numero")

print(f"la conversion a nota chilena es {conversion_puntaje(p, pt)}")