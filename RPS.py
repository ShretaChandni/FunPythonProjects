import random
seq = ('r', 'p', 's')
random.choice(seq)

mapping = {
    'r':'🌚',
    'p': '📰',
    's': '✂'
}
win = True
while win == True:
    x = input('Rock, paper or scissors? (r/p/s): ')
    print(f'You chose {mapping.get(x)}')
    y = random.choice(seq)
    print(f'Computer chose {mapping.get(y)}')
    if x == y:
        print('Game Draw')
    elif x == 'r' and y == 'p':
        print('You loose')
        win = False
    elif x == 's' and y == 'p':
        print('You won')
    elif x == 'r' and y =='s':
        print('You won')
    else:
        print('You loose')
        win = False
