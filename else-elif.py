num = 60
if num <= 50:
    print('The nmber is less than or equal to 50')
else:
    print('this number is greater than 50')


output = 'The number is less than equal to 50' if num <= 50 else 'The number is greater than 50'
print(output) # da The number is greater than 50

# elif
light = 'Red'
if light == 'Green':
    print('Go')
elif light == 'Yellow':
    print('Caution')
elif 1 == 1:
    print('Amazing') # python para en la primera condition verdadera que encuentre
elif light == 'Red':
    print('Stop')
else:
    print('incorrect light signal')