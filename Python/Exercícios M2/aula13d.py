n = int(input('Digite um número qualquer: '))
print('\033[34m-=-\033[m'*6)
print(f'\033[33mA tabuada de {n} é:\033[m')
print('\033[34m-=-\033[m'*6)
for c in range (0, 11):
    print(f'\033[97;41m{n} x {c:2} = {n*c:2}\033[m')
    print('')
print('\033[34m-=-\033[m'*6)
