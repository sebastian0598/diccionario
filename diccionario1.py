def menu():
    print('1. agregar')
    print('2. Imprimir')
    print('3. Eliminar')
    print('4. Consultar')
    print('5. salir')
    opcion = input('bienvenidos que desea hacer? ')
    return opcion

def main():
    while True:
        opcion=menu()
        if opcion == '1':
            print('agregar funcionario')
            cont = 0
            while True:

                diccionario = {
                    
                        'id': input("digite el id del ususario: "),
                        'nombre' : input("digite el nombre del usuario: "), 
                        'cargo': input("digite el cargo del usuario: "), 
                        'salario': int(input("digite el salario del usuario: "))
                }
                cont = cont + 1
                continuar = bool(input("estriba True si desea ir al menu: "))
                if continuar == True:
                    break

        
        elif opcion == '2':
            print('imprimir datos del funcionario')
            print(diccionario)

            
        elif opcion == '3':
            eliminar = (input("digite el funcionario que desee eliminar: "))
            
            if eliminar not in diccionario:
                print("este dato no se encuentra")
            else:
                del diccionario[eliminar]
                print('ELIMINADO')

        elif opcion == '4':
            busca=input('introduce la busqueda: ')
            print('resultado: ',diccionario.get(busca,'no encontramos nada'))
        elif opcion == '5':
            print("saliendo")
            break    
main()



