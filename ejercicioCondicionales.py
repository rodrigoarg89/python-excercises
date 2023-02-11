#Tenda de descuento Black Friday
'''
- si el precio es 300 o mas aplica un 30% de descuento
- si el precio esta entre 200 y 300 (incluyendo 200) aplica un 20% de descuento
- si el precio esta entre 100 y 200( incluyendo el 100) aplica un 10-% de descuento
- si el precio es menos que 100 aplica un 5% de descuento
- si el precio es negativo no habra descuento
'''
price = 300

if price >= 300:
    price *= 0.7
    print('with -30%, its price is:', price)
elif price >= 200:
    price *= 0.8
    print('with -20%, its price is:', price)
elif price >= 100:
    price *= 0.9
    print('with -10%, its price is:', price)
elif price < 100 and price >= 0:
    price *= 0.95
    print('with -5%, its price is:', price) 
elif price < 0:
    print('Without discount')
else:
    print('enter price correctly')