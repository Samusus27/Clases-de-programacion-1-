  Cajero Automatico

saldo = 0
opc = None
seguir = "S"
print("Bienvenido(a) a su banco de confianza")

while(seguir != 'n' and seguir != 'N'):
    opc = int(input("-Digite 1 si desea realizar un deposito" "\n-Digite 2 si desea retirar dinero en efectivo\n-Digite 3 si desea ver su saldo actual"))
    if(opc == 1):
        for i in range(1):
            depo = float(input("Digite el monto que desea depositar a su cuenta\n₡"))
            saldo += depo
            print("Su deposito se ha realizado con exito")
            seguir = str(input("¿Desea realizar otra transacción?  S/N"))
    elif(opc == 2):
        for i in range(1):
            reti = float(input("Digite el monto que desea retirar:\n₡"))
            if(reti > saldo):
                print("Fondos insuficientes")
            else:
                saldo -= reti
                print("Su retiro se ha realizado con exito")
            seguir = str(input("¿Desea realizar otra transacción?  S/N"))
    elif(opc == 3):
        print("Su saldo es:\n₡",saldo)
        seguir = str(input("¿Desea realizar otra transacción?  S/N"))
print("transacción finalizada\nSu saldo es de ₡",saldo,"\nPor favor retire su tarjeta")
                  
