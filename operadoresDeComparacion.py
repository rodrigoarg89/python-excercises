num1 = 5
num2 = 10 
num3 = 10

list1 = [6, 7, 8]
list2 = [6, 7, 8]

print(num1 > num2)

print(num2 is not num3) # true
print(list1 is list2) # false

print(id(num2)) # tienen el mismo id
print(id(num3))

print(id(list1)) # TIENEN DIFERENTE ID, Python crea otro espaciio en memoria para el objeto
print(id(list2))


