phone_book = {
    'Batman' : 456525,
    'Sensei' : 455512,
    'Gohsbuster' : 44516
}

# agragr un elemento
phone_book['Gotzila'] = 456552
print(phone_book)

# editar un elemento
phone_book['Gotzila'] = 90000
print(phone_book)

# eliminar batman
del phone_book['Batman']
print(phone_book)


#eliminar un elemento en especifico
Sensei = phone_book.pop('Sensei')
print(phone_book)
print(Sensei) #imprime el valor de sensei

#si queremos ademas la llave de el ULTIMO ELEmento añadido
gotzila = phone_book.popitem()
print(phone_book)
print(gotzila) # me da Gotzila: 90000

# cuanto item tiene mi diccionario
phone_book = {
    'Batman' : 456525,
    'Sensei' : 455512,
    'Gohsbuster' : 44516
}
print(len(phone_book))

# comprobar si exite una llave en mi diccionario
print('Batman' in phone_book) # true
print('Gotzila' in phone_book) # false

# agregar otro diccionario a mi diccionario actual
second_phone_book = {
    'Goku' : 458854,
    'Vegeta' : 625514
}
phone_book.update(second_phone_book)
print(phone_book) # {'Batman': 456525, 'Sensei': 455512, 'Gohsbuster': 44516, 'Goku': 458854, 'Vegeta': 625514}

