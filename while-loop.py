# while

n = 2
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
print(power) # 9

'''otro ejemplo'''
n = 249
last = n % 10
print(last)# 9

first = n #249
while first >= 10:
    first = first // 10 #24 # 2
    print(first) # 24 # 2

print(last + first)# 11


'''otro ejemplo'''
# while True:
    # print('Hello word') # imprime hello world indefinidamente

'''conrchetes balanceados'''
brackets = '[[[]][]]]'
# crear una variable para contar los corchetes abiertos
open_count = 0
# crear otra varible que me va a servir como incide para iterar sobre el string
bracket = 0

while bracket < len(brackets):
    #si encontramos un corchete de apertura, aumentamos la cuenta de corchetes abiertos
    if brackets[bracket] == '[':
        open_count += 1
    elif brackets[bracket] == ']':
        open_count -= 1
    if open_count < 0:
        print('no esta balanceado')
        break 
    bracket += 1

    
if open_count == 0:
    print('Está totalmente balanceada')
else:
    print('no esta balanceada')



