a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1
a = 1
while a < 10:
    print(f'{an} -> ', end='')
    an += r
    a += 1
print('FIM')
