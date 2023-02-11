num_list = []

'''append añade un elemento al final de la lista'''
num_list.append(1)
num_list.append(2)
print(num_list)

'''insertar un elemento en una poscion determinada'''
num_list = [1, 2, 3, 4, 5]
num_list.insert(3, 4) # en la posicion 3 agrego el 4, me [1, 2, 3, 4, 4, 5]
print(num_list)


'''eliminar el ultimo elemento de una lista'''
clubs = ['River', 'Boca', 'Velez', 'Racing', 'Boca', 'Talleres' ]
last_club = clubs.pop()
print(clubs) # ['River', 'Boca', 'Velez', 'Racing']
print(last_club) # Talleres

'''eliminar el primer elemento que encuentre de una lista'''
clubs.remove('Boca')
print(clubs) # ['River', 'Velez', 'Racing']

'''ordenar una lista al reves'''
num_list = [1, 2, 3, 4, 5]
num_list.reverse()
print(num_list)


'''ordenar una lista de menor a mayor'''
num_list = [11, 2, 3, 4, 5]
num_list.sort()
print(num_list)
'''ordenar una lista mayor a menor'''
num_list = [11, 2, 3, 4, 5]
num_list.sort(reverse=True)
print(num_list)



'''Slicing'''
num_list = [1, 2, 3, 4, 5]
print(num_list[2:5]) # me da [3, 4, 5]

'''Index'''
cities = ['BsAs', 'Cordoba', 'Salta']
print(cities.index('Cordoba'))
print(cities[2])


''' para saber si esta mi lista'''
print('BsAs' in cities) # da true
print('Bogota' in cities) # da false