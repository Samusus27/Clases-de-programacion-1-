# Solicitar un monto y basado en ese monto aplicaremos una serie de descuentos
# Si el monto está entre 20mil y 30mil aplicamos un 10%
# Si el monto es mayor igual a 30mil y 50mil aplicamos un 15%
# Si el monto es mayor igual a 50mil y 80mil aplicamos un 20%
# en caso contrario aplicaremos un 5%

monto = int(input("Digita un monto "))

if(monto >= 20000 and monto < 30000):
    dto = monto * 0.10
elif(monto >= 30000 and monto < 50000):
    dto = monto * 0.15
elif(monto >= 50000 and monto < 80000):
    dto = monto * 0.20
else:
    dto = monto * 0.05
total = monto - dto
print("El descuento es de  ",dto,"\nEl total a pagar es ",total)

    
