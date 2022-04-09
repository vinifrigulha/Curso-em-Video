from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Escolha:
[ 0 ] para PEDRA;
[ 1 ] para PAPEL
[ 2 ] para TESOURA.''')
jogador = int(input('Digite: '))
computador = randint(0, 2)
print('JO...', end = '  ')
sleep(1)
print('KEN...', end = '  ')
sleep(1)
print('PÔOOOO!!!')
sleep(1)
print(f'O computador jogou {itens[computador]} e você {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATAMOS! Vamos de novo!')
    elif jogador == 1:
        print('AH NÃO!! Você me venceu!')
    else:
        print('AH HÁ! Eu venci!! Tente de novo!')
elif computador == 1:
    if jogador == 0:
        print('AH HÁ! Eu venci!! Tente de novo!')
    elif jogador == 1:
        print('EMPATAMOS! Vamos de novo!')
    else:
        print('AH NÃO!! Você me venceu!')
else:
    if jogador == 0:
        print('AH NÃO!! Você me venceu!')
    elif jogador == 1:
        print('AH HÁ! Eu venci!! Tente de novo!')
    else:
        print('EMPATAMOS! Vamos de novo!')