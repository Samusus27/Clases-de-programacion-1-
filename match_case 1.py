monto = int(input("Digite un monto "))
print("Menu: \n1.Azul \n2.Rojo \n3.Amarillo \n4.Verde \n5.Blanco")
opc = int(input("Digite el numero que corresponde al color"))

match(opc):
    case 1:
        dto = monto * 0.20
    case 2:
        dto = monto * 0.30
    case 3:
        dto = monto * 0.35
    case 4:
        dto = monto * 0.40
    case 5:
        dto = 0
total = monto - dto
print("El descuento es de ¢ ",dto, "\nTotal a pagar ¢", total)
