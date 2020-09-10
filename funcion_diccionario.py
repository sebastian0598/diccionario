#insertar
diccionario = {
                    
    'id': input("digite el id del ususario: "),
    'nombre' : input("digite el nombre del usuario: "), 
    'cargo': input("digite el cargo del usuario: "), 
    'salario': int(input("digite el salario del usuario: "))
}
#mostrar
print(diccionario)
#eliminar
eliminar = (input("digite el funcionario que desee eliminar: "))
del diccionario[eliminar]
#buscar
busca=input('introduce la busqueda: ')
print('resultado: ',diccionario.get(busca,'no encontramos nada'))