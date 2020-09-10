#eliminar
eliminar = (input("digite el funcionario que desee eliminar: "))
del diccionario[eliminar]
#buscar
busca=input('introduce la busqueda: ')
print('resultado: ',diccionario.get(busca,'no encontramos nada'))
#mostrar
print(diccionario)