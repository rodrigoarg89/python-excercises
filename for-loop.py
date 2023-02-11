number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in number_list:
  if number %2 == 0:
    print('este nmero es par:', number)
  else:
    print('este numer es impar', number ) 



print('otro ejemplo -------------------------------------------------')

max_odd_numbers = 0
for number in range(1, 23):
  if number %2 == 0:
    print('este nmero es par:', number)
  else:
    print('este numer es impar', number ) 
    max_odd_numbers +=1

print('la cantidad maxima de numeros impares es:', max_odd_numbers)


print('otro ejemplo -------------------------------------------------')
n = 50
num_list = [10, 25, 23, 4, 6, 18, 27, 42]
found = False

for number_1 in num_list:
  for number_2 in num_list:
    if number_1 != number_2:
      if number_1 + number_2 == n:
        found = True # esto es para que no se me imprima dos veces mi resultado 23 27 y 27 23
        break
  if found: # si existe found, es decir si es true
        print(number_1, number_2)
        break


print('otro ejemplo -------------------------------------------------')
num_list = list(range(0, 9))

for number in num_list:
  if number == 3 or number == 6 or number == 8:
    continue
  print(number) # no se imprime NI 3 6 ni 8
        