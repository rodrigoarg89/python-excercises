random_string = 'I am Batman'
print(len(random_string))
'''cantidad de caracteres 11'''

'''indexing'''
var_1 = 'hello'
print(var_1[2]) #l la ele
print(var_1[4]) #o la o

var_2 = 'Nicolas'
print(var_2[-1]) #s la letra s

last = var_2[len(var_2)-1]
print(last) #s letra s

'''slicing'''
my_string = 'This is my string'
print(my_string[0:4]) # em da This
print(my_string[1:7]) # me da his is
print(my_string[8:len(my_string)]) # me da my string
print(my_string[8:400]) # me da my string
print(my_string[0:7]) # me da This is
print(my_string[0:7:1]) # me da This is cntando de 1 en 1
print(my_string[0:7:2]) # me da Ti s contando de 2 en 2

print(my_string[:8]) # me da This is 
print(my_string[8:]) # me da my string
print(my_string[:]) # me da This is my string

print(my_string[::-1]) # me da gnirts ym si sihT al reves

''' los string son inmutables, mas no las variables N SE PUEDEN CAMBIAR LOS caracteres, pero si puedo asignarle valor a todo el string nuevamente'''
print(my_string[0]) #T







