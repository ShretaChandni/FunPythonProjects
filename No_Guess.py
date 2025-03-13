
number = 66
attempt = 0
while attempt <5: 
    attempt += 1
    x = (input('Gusee the number : (or type Quit to exit'))
    if x == ('Quit'):
        print('Thanks for palying!')
        break
    if int(x) == number:
        print('Congratulation! you have won within the first 5 attempt')
        break
    elif int(x) > number:
        print('OOPs! Number is too high, try again')
        continue
    elif int(x) < number:
        print('OOPs! Number is too low, try again')
        continue
    elif type(x) != int:
        print('Invalid format, try again')
        continue
