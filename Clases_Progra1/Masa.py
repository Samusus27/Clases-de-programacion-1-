#Masas: Solicitar los datos de presión, volumen y temperatura, posteriormente imprimir el valor de la masa de aire:
valor1 = float(input("Digite el valor de la presión del aire "))
valor2 = float(input("Digite el valor del volumen del aire "))
valor3 = float(input("Digite el valor de la temperatura del aire "))
masa= ((valor1 * valor2) / (0.37 * valor3 + 460))
print("la masa del aire es",masa)
 
