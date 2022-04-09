msg = '10 PRIMEIROS TERMOS'
print('='*25)
print(f'{msg:^25}')
print('='*25)
a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
a10 = a1 + 9*r
for n in range(a1, a10+r, r):
    print(f'{n}', end = ' → ')
print('ACABOU!')