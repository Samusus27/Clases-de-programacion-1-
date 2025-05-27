while(True) :
    try:
        num1 = int(input("Digite un numero "))
        num2 = int(input("Digite otro numero "))
        resultado = num1 + num2
        print("La suma del resultado es: ",resultado)
        break;
    except:
        print("Debe digitar numeros con decimales")
        
