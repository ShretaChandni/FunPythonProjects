x = int(input('Enter the amount: '))
s = input('Source currency (USD/EUR/CAD): ')
t = input('Target currency (USD/EUR/CAD): ')

if  s == ('USD') and t == ('EUR') or s == ('EUR') and t == ('USD'):
    y = (x/0.92)
    print(f'{x} is {y}')
elif s == ('USD') and t == ('CAD') or s == ('CAD') and t == ('USD'):
     y = (x*1.44)
     print(f'{x} is {y}')
elif s == ('CAD') and t == ('EUR') or s == ('EUR') and t == ('CAD'):
     y = (x/0.95)
     print(f'{x} is {y}')
else:
    print('invalid format')
