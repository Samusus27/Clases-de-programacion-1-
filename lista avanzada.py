Lista = [ ]
opc = 0

while(opc != 8):
    print("Menu")
    print("1.Capturar datos")
    print("2.Mostrar datos")
    print("3.Agragar dato")
    print("4.Eliminar un dato")
    print("5.Modificar un dato")
    print("6.Elemento mayor y elemento menor")
    print("7.Lista inversa")
    print("8.Salir")

    opc = int(input("Digite una opción: "))
    match(opc):
        case 1:
            for i in range(5):
                print("Ingrese un elemento en el índice ",i)
                elemento =input()
                Lista.insert(i,elemento)
        case 2:
            print("Los elementos de la lista son: \n",Lista)
        case 3:
            elemento = input("Ingrese el elemento que desea agregar: ")
            ind = int(input("Ingrese el indice donde desea agregar el elemento: "))
            longitud = int(len(Lista))
            if(ind>longitud or ind < 0):
                print("El indice debe de estar entre 0 y ",longitud)
            else:
                Lista.insert(ind,elemento)
                print("Elemento agregado!!")
        case 4:
            ind = int(input("Ingrese el indice del elemento que desea eliminar: "))
            longitud = int(len(Lista))
            if(ind>longitud or ind < 0):
                print("El indice debe de estar entre 0 y ",longitud)
            else:
                del Lista[ind]
                print("Elemento eliminado!!")
        case 5:
            elemento = input("Ingrese el elemento que desea modificar: ")
            ind = int(input("Ingrese el indice donde desea modificar el elemento: "))
            longitud = int(len(Lista))
            if(ind>longitud or ind < 0):
                print("El indice debe de estar entre 0 y ",longitud)
            else:
                Lista[ind] = elemento
                print("Elemento modifica!!")
        case 6:
            print("El elemento menor de la lista es: ",min(Lista))
            print("El elemento mayor de la lista es: ",max(Lista))
        case 7:
            print("La lista de manera inversa es: ")
            Lista.reverse()
            print(Lista)
            Lista.reverse()
        case 8:
            print("Programa terminado!!")
        case _:
            print("Opcion invalida")
            
                    
                
            
