a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1
a = 1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while a < total:
        print(f'{an} -> ', end='')
        an += r
        a += 1
        c += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print(f'Você exibiu {c} termos dessa PA.')