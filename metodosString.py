# CAPITALIZE
txt = 'hello welcome to Academlo'
x = txt.capitalize() # convierte la primera letra en mayuscula
print(x)
'''txt.capitalize() esto asi no funciona xq los string son inmutables'''

txt = 'Python es divertido'
print(txt)

txt = '27 is my age'
print(txt)



# CASE FOLD
txt = 'Hello and welcome to Academlo'
x = txt.casefold() # la primera se convierte en minuscula
print(x)




# LOWER igual que el anterior
x = txt.lower() # la primera se convierte en minuscula
print(x)




# CENT retorn un string centrado
txt = 'Pinaple'
x = txt.center(20) #centrado en 20 caracteres
print(x)

x = txt.center(20, 'x')  #centrado en 20 caracteres con xxxx
print(x)




# COUNT contar cuantas veces aparece un string en una cadena
txt = 'I love watermelons, watermelons are my favorite fruit'
x = txt.count('watermelons')
print(x) # 2 (vces)
print(type(x)) # class 'int'



# ENDSWITH termina con ''
txt = 'Hello, welcome to my world.'
x = txt.endswith('.')
print(x) # da true
x = txt.endswith('my world', 5,11)
print(x) # da false

x = txt.endswith('my world.', 5,100) #desde el caracter 5 hasta el caracter posicion 100
print(x) # da true




# FIND busca una palabra y nos dice donde esta
txt = 'Hello, welcome to my world.'
x = txt.find('welcome')
print(x) # me da 7, apartir del indice 7 ya esta la palabra welcome

# INDEX
txt = 'Hello, welcome to my world.'
x = txt.index('welcome')
print(x) # me da 7 igual q el anteiror



# ISLOWER todo esta en minusculas? da true o false
txt = 'Hello, welcome to my world.'
x = txt.islower() # da false
print(x)



# UPPER / ISUPPER
txt = 'Hello, welcome to my world.'
x = txt.upper() # pasa todo a mayusculas
print(x)

x = txt.upper().isupper() # da true
print(x)

x = txt.upper().lower().islower() # da true
print(x)

x = txt.isupper() # todo esta en mayusculas? true o false
print(x) # da false, no esta todo en mayusculas


#comvertir la primera letra de cada palabra en mayuscula
txt = 'hola a todos desde academlo'
x = txt.title()
print(x) # da Hola A Todos Desde Academlo
print(x.istitle()) # da true


#reemplazar valores
txt = 'hola a todos desde academlo'
x = txt.replace('academlo', 'Colombia')
print(x) # da hola a todos desde Colombia


#convertir en una lista []
print('para convertir en una lista []')
txt = 'hola a todos desde academlo'
x = txt.split(' ')
print(x) # da ['hola', 'a', 'todos', 'desde', 'academlo']

txt = 'hola,a,todos,desde,academlo'
x = txt.split(',')
print(x) # da ['hola', 'a', 'todos', 'desde', 'academlo']


# para volver a tener mi strign como era
print('para volver a tener mi strign como era')
txt = 'hola a todos desde academlo'
x = txt.split()
print(x) # da ['hola', 'a', 'todos', 'desde', 'academlo']
z = ' '.join(x)
print(z) # da hola a todos desde academlo
z = '-'.join(x)
print(z) # hola-a-todos-desde-academlo





# IS NUMERIC
txt = '13164652'
print(txt.isnumeric()) # da true~
