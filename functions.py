# functions

def mi_funcion(parametro_1, parametro_2):
    variable = 'Hola'
    print(variable)
    return variable

mi_funcion('verde', 5) # no retorna nada

'''other example'''

color = 'red'
def find_minimum(first:int, second:int=0, name:str='') -> int: # valores por defecto lo agregamos al
    #-> va a retornar un entero
    color = 'blue'
    print('hola:', name)
    print(color) # impirme primero este color x el scope
    if first < second:
        return first
    return second

# find_minimum(3, 4)

num_1 = 110
num_2 = 20
result = find_minimum(num_1, num_2, name='Andrea')
print(result)
print(color)