#Solicitar al usuario el nombre y las horas laboradas al mes, posteriormente el sistema calcula el salario bruto
#la deduccion de la caja y el salario neto
nombre = str(input("Digite su nombre"))
hl = int(input("Digite sus horas laboradas en el mes"))
precio = 4000
sb = hl * precio
ccss = sb * 0.10
sn = sb - ccss
print(nombre,"Su salario base es de ¢ ",sb,"\nSu deduccion es de ¢",ccss)
print("Su salario neto de ¢ ",sn)
