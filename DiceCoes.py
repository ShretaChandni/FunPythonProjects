import random

seq = range(1, 7)

random.choice(seq)

def function():
    xrando = random.choice(seq)
    yrando = random.choice(seq)
    return(xrando, yrando)
while True:
    x = input('Roll the dice? (y/n): ')
    if x == ('y'):
        print(function())
    elif x == ('n'):
        print('Thanks for playing!')
        break
    else:
        print('invalid input')
