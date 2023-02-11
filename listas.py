lista = ['Hola soy una lista', 45, ['Argentina', 'Peru', 'Brasil'], 4.5]

lista[2] = 'He cambiado de valor'
print(lista)

lista[1] += 10
print(lista)


'''otra forma de aladir elementos en una lista'''
num_seq = range(0, 10) #va desde el 0 hasta el 10-1
print(num_seq)

num_seq = list(num_seq)
print(num_seq)

num_seq = range(3, 20, 3)
print(num_seq)
print(list(num_seq))

'''accediendo a elementos dentro de un objeto en python'''
world_cup_winners = [
    [2006, 'Italy'],
    [2010, 'Spain'],
    [2014, 'Germany'],
    [2018, 'France']
]

france = world_cup_winners[3][1]
print(france) #france

part_A = [1, 2, 3, 4, 5]
print(len(part_A))
part_B = [6, 7, 8, 9]
merged_list = part_A + part_B
print(merged_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

part_A.extend(part_B)
print(len(part_A))
print(part_A)