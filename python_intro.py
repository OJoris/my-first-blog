#if 5>2:
#    print('5 is indeed greater than 2')
#else:
#    print('5 is not greater than 2')

def hi(name):
#name = 'Olly'
#    if name == 'Olly':
        print('hey ' + name + '!')
#    elif name == 'Bob':
#        print('hey Bob!')
#    else:
#        print('hey anonymous!')

#hi('Bob')

girls=['Rachel', 'Monica', 'Phoebe', 'Ola', 'Olly']

for name in girls:
    hi(name)
    print('next girl')
