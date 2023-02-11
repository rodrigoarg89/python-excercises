''''comparacion, asignacion, aritmeticos, logicos'''

#operadores aritemticos

'''adicion'''
print(10+5)

float_1 = 13.5
float_2 = 5.2
print(float_1 + float_2)

num = 10
print(float_1 + num) # el result es otro flotante


'''sustraccion'''
print(10-2)
float_3 = -10.25
float_4 = 3.5
print(float_3 - float_4) # -13.75
print(float_4 - float_3) # 13.75

print(float_3 - num) # -20.25

'''multiplicacion'''
print(40 * 10) # 400
print(float_3 * float_4) # -35.875

print(float_3 * num) # -102.5


'''division'''
print(40 / 10) # 4.0 simepre se obtiene un flotante
print(float_3 / float_4) # -2.92

print(float_3 / num) # -1.025

'''division entera'''
print(40 // 10) # 4.0 simepre se obtiene un ENTERO
print(12.4//2) # me da 6.0 un flotante la division entre un float y un entero
print(int(12.4//2)) # lo convertimoa a entero 6

'''operador modulo'''
print(10 % 2) # da 0
print(11 % 2) # da 1
print(-28 % 2) # da 0
print(28.5 % 2.5) # da 1.0 un flotante

'''Procedencia o el orden a seguir'''
print(10-3*2) # primero va la multi
print(10*3/2) # primero va la multi, me da 15.0


'''Parentesis'''
print(10*(3/6)) # da 5.0