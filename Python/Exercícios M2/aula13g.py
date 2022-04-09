num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c != 0:
        print(f'\033[31m{c}\033[m ', end = '')
    else:
        print(f'\033[33m{c}\033[m ', end = '')
        cont += 1
if cont == 2:
    print(f'\nO número {num} tem 2 divisores, logo ele É PRIMO.')
else:
    print(f'\nO número {num} tem {cont} divisores, logo NÃO É PRIMO.')
