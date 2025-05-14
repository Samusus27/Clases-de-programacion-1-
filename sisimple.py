monto = int(input("Digite un monto"))

if(monto >= 12000):
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

print("El descuento es de",int(descuento))
print("El total a pagar es de",int(total))
