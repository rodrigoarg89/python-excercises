'''Concatenacion usando
el operador +
el operador %
metodo format
f-Strings
join'''

name = "Juna Jose"
lastname = 'Lozano'
full_name = name + " "+ lastname
print(full_name)

result = 1 + 2
print(result)

text = "El resultado de 1 + 2 es:" + str(result)
print(text)


'''' con el operadot modulo'''
brand = 'Academlo'
text2 = "Hola %s" % brand
print(text2)

'''si quiero concatenar muchas variables'''
my_name = 'Rodrigo'
text2 = "Hola %s mi nombre es %s" % (brand, my_name)
print(text2)

''''Metodo format'''
var_1 = 'stoy aprendiendo'
var_2 = 'Python'

text ='{} {}'.format(var_1, var_2)
print(text) 
'''stoy parendiendo python'''

text ='{1} {0}'.format(var_1, var_2)
print(text)
'''python stoy aprendiendo'''

text ='{var_make} {var_programming}'.format(var_make = var_1,
                                        var_programming = var_2)
print(text) 


'''f-strings'''
favorite_food = 'paste'
name4 = 'NICOLAS'
text4 = f'La comida favorita de {4+5} es {2+3}'
text4 = f'La comida favorita de {name4} es {favorite_food}'
print(text4)

'''join'''
cadena = ['Hola', 'Nicolas', 'Rondon']
text5 = ' '.join(cadena)
print(text5)