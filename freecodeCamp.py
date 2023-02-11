# inp = input('Europe floor?')
# usf = int(inp) + 1
# print('US floor', usf)


'''Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours'''
# xh = input('Enter Hours: ')
# xr = input('Enter Rate: ')

# fh = float(xh)
# fr = float(xr)

# if fh > 40 :
#     print('Overtime')
#     reg = fr * fh
#     otp = (fh - 40.0) * (fr * 0.5)
#     print(reg, otp)
#     xp = reg + otp
# else:
#     print('Regular'
#     )
#     xp = fh * fr
# print('Pay:', xp)  


'''Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:'''

# xh = input('Enter Hours: ')
# xr = input('Enter Rate: ')
# try:
#     fh = float(xh)
#     fr = float(xr)
# except:
#     print('Error, please enter numeric input')
#     quit() #para que no aparezca el error

# if fh > 40 :
#     print('Overtime')
#     reg = fr * fh
#     otp = (fh - 40.0) * (fr * 0.5)
#     print(reg, otp)
#     xp = reg + otp
# else:
#     print('Regular'
#     )
#     xp = fh * fr
# print('Pay:', xp)  


'''other exercise : Which line/lines should be surrounded by try block? respuest 3, 4'''

# temp = "5 degrees"
# cel = 0
# try:
#     fahr = float(temp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
# except:
#     quit()
# print(cel)

'''Arguments in the function vs parameters'''

# def greet(lang):
#     if lang == 'es':
#         print('Hola')
#     elif lang == 'fr':
#         print('Bojour')
#     else:
#         print('Hello')

# greet('en')
# greet('fr')
# greet('es')

'''Multiple parameters'''
# def addtwo(a, b):
#     added = a + b
#     return added

# x = addtwo(3, 5)
# print(x)

'''Lopps and iterations'''

# n = 5
# while n > 0:
#     print(n)
#     n = n-1
# print('finished')
# print(n)

'''infinite loop'''
# n = 5
# while n > 0:
#     print('Rodrigo') # print Rodrigo eternamente, ya que la n es siempre  mayor que cero
# print('Dry off')

'''Breaking out of a loop'''
# while True:
#     line = input('> ') # mientras escriba en la entrada > cualquier entrada el codigo se ejecutara, pero al escribir done se producira un break y se impimira un Done, el codigo habra terminado
#     if line == 'done':
#         break
#     print(line)
# print('Done')

'''Finishing an iteration with continue'''
# while True:
#     line = input('> ') 
#     if line[0] == '#': 
#         continue 
#     # si escribimos x ejemplo # no impirmas esto, como contiene #, no se imprimira pero el codigo continuara para poder seguir rescribiendo mas entradas
#     if line == 'done':
#         break 
#     print(line)
# print('Done')


'''definite loop'''
# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('finished')

# friends = ['Joseph', 'Glen', 'Sally']
# for friend in friends:
#     print('Happy New year:', friend)
# print('Done')

'''for i in sequence'''
for i in [5, 4, 3, 2, 1]:
    print(i)