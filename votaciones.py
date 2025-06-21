edad =  int(input("Digite su edad"))
nac = str(input("Digite su nacionalidad"))

if(edad >= 18 and nac == "costarricense" or nac == "Costarricense" or
   nac == "COSTARRICENSE" or nac == "Tico" or nac == "TICO" or nac == "tico"):
    print("Puede votar")
else:
    print("Usted no puede votar")
    
